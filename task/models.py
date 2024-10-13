from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Task(models.Model):
    BACKLOG_STATUS = 'B'
    IN_PROGRESS_STATUS = 'I'
    DONE_STATUS = 'D'

    TASK_STATUSES_CHOICES = (
        (BACKLOG_STATUS, 'Backlog'),
        (IN_PROGRESS_STATUS, 'In Progress'),
        (DONE_STATUS, 'Done')
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=TASK_STATUSES_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title