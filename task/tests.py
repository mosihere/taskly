from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from task.models import Task

User = get_user_model()

class TaskAPITests(APITestCase):
    
    def setUp(self):
        # Create regular users
        self.user1 = User.objects.create_user(
            phone_number='1234567890',
            password='password123'
        )
        self.user2 = User.objects.create_user(
            phone_number='0987654321',
            password='password123'
        )

        # Obtain JWT tokens for user1
        self.token1 = RefreshToken.for_user(self.user1).access_token
        self.token2 = RefreshToken.for_user(self.user2).access_token

        # Set the authorization header for user1
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(self.token1))

        # Create a task for user1
        self.task1 = Task.objects.create(
            title="User 1's Task",
            status=Task.BACKLOG_STATUS,
            user=self.user1
        )
    
    def test_create_task(self):
        """
        Ensure a logged-in user can create a task
        """
        url = reverse('task:task-list')
        data = {
            "title": "New Task",
            "status": Task.IN_PROGRESS_STATUS
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.last().title, "New Task")
        self.assertEqual(Task.objects.last().user, self.user1)

    def test_get_task(self):
        """
        Ensure a user can retrieve their own task
        """
        url = reverse('task:task-detail', kwargs={'pk': self.task1.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task1.title)

    def test_update_task(self):
        """
        Ensure a user can update their task
        """
        url = reverse('task:task-detail', kwargs={'pk': self.task1.id})
        data = {
            "title": "Updated Task",
            "status": Task.DONE_STATUS
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Updated Task")
        self.assertEqual(self.task1.status, Task.DONE_STATUS)

    def test_delete_task(self):
        """
        Ensure a user can delete their task
        """
        url = reverse('task:task-detail', kwargs={'pk': self.task1.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_user_cannot_access_others_tasks(self):
        """
        Ensure a user cannot retrieve, update, or delete another user's task
        """
        # Authenticate user2 with their JWT
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(self.token2))  

        # Use the task created for user1
        url = reverse('task:task-detail', kwargs={'pk': self.task1.id})

        # User2 trying to retrieve user1's task
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # User2 trying to update user1's task
        data = {"title": "Illegal Update"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # User2 trying to delete user1's task
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_tasks(self):
        """
        Ensure a user can filter tasks by title and created date.
        """
        # Clean up any existing tasks for user1
        Task.objects.filter(user=self.user1).delete()

        # Create additional tasks for user1
        Task.objects.create(title="Task A", status=Task.BACKLOG_STATUS, user=self.user1)
        Task.objects.create(title="Task B", status=Task.IN_PROGRESS_STATUS, user=self.user1)
        Task.objects.create(title="Task C", status=Task.DONE_STATUS, user=self.user1)

        url = reverse('task:task-list')

        # Test filtering tasks by title using icontains
        response = self.client.get(url, {'title': 'Task A'})  # Filter by title
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure that there is at least one match and verify its title
        self.assertGreater(len(response.data), 0)  # There should be matches
        task_titles = [task['title'] for task in response.data]
        self.assertIn("Task A", task_titles)  # Check that "Task A" is one of the returned titles