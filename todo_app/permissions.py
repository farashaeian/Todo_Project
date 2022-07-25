from rest_framework import permissions
from .models import Task


class ChangePermission(permissions.BasePermission):
    message = 'Impossible'

    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH']:
            if Task.objects.get(id=request.parser_context['kwargs']['pk']).done is True:
                return False
        return True
