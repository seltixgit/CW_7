from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ Проверяем, является ли пользователь владельцем."""
    def has_object_permission(self, request, view, obj):
        print("IsOwner")
        if obj.owner == request.user:
            return True
        return False
