from rest_framework import permissions

class GlobalPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            ...
        
        if request.method == 'POST':
            ...

        if request.method == ['PUT']

        return False
