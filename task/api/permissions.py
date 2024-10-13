from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to allow authenticated users to modify only their own tasks,
    and admin users to have full access (CRUD) on all tasks.
    """
    
    def has_permission(self, request, view):
        # Authenticated users can view the list or create tasks
        if request.method in SAFE_METHODS or request.method == 'POST':
            return bool(request.user and request.user.is_authenticated)
        return True

    def has_object_permission(self, request, view, obj):
        # Admin users have full access
        if request.user.is_staff:
            return True
        # Otherwise, check if the user is the owner of the task
        return obj.user == request.user