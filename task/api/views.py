from task.models import Task
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .permissions import IsOwnerOrAdmin



class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):

        if self.request.user.is_staff:
            return Task.objects.select_related('user').all()
        
        return Task.objects.select_related('user').filter(user=self.request.user)