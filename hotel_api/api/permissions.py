from rest_framework import BasePermission


class NotAdminUser(BasePermission):
    """
    Custom permission to grant access only to non-admin users
    """
    
    def has_permission(self, request, view):
        return not request.user.is_staff