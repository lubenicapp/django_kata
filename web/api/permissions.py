from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class CustomPatchPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            if request.headers.get('Authorization') != 'Magic_Key':
                raise PermissionDenied(detail="La force n'est pas avec toi")
        return True
