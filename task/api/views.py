from task.models import Task
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .permissions import IsOwnerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter



class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):

        if self.request.user.is_staff:
            return Task.objects.select_related('user').all()
        
        return Task.objects.select_related('user').filter(user=self.request.user)