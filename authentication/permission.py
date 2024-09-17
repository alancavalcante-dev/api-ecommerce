from rest_framework import permissions


MAP = {
    'GET': 'view',
    'OPTIONS': 'view',
    'HEADER': 'view',
    'POST': 'add',
    'PUT': 'change',
    'PATCH': 'change',
    'DELETE': 'delete'
}


class GlobalPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):

        if hasattr(view, 'queryset'):
            model = view.queryset.model
        elif hasattr(view, 'model'):
            model = view.model
        else:
            return False 
        
        app_label = model._meta.app_label

        
        if request.method in permissions.SAFE_METHODS:
            permission = f'{app_label}.{MAP['GET']}_{model._meta.model_name}'
            return request.user.has_perm(permission)
        
        if request.method == 'POST':
            permission = f'{app_label}.{MAP['POST']}_{model._meta.model_name}'
            return request.user.has_perm(permission)

        if request.method == ['PUT', 'PATCH']:
            permission = f'{app_label}.{MAP['PUT']}_{model._meta.model_name}'
            return request.user.has_perm(permission)
        
        if request.method == 'DELETE':
            permission = f'{app_label}.{MAP['DELETE']}_{model._meta.model_name}'
            return request.user.has_perm(permission)

        return False
