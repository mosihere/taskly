from rest_framework.routers import DefaultRouter
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import TaskViewSet

# Define the router and register the TaskViewSet
router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

# Set up the schema view for Swagger and Redoc
schema_view = get_schema_view(
    openapi.Info(
        title="Task Management API",
        default_version='v1',
        description="API documentation for the Taskly",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

# Combine the API routes with the documentation routes
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Include the router's routes
urlpatterns += router.urls