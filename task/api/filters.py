from django_filters.rest_framework import FilterSet
from task.models import Task



class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'title': ['icontains'],
            'created_at': ['gt', 'lt']
        }