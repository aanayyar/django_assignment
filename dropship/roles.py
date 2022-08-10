
from rest_framework.permissions import BasePermission

       
class ProjectManager(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user and request.user.groups.filter(name="ProjectManager") or request.user.is_staff:
            return True
        return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
         if request.method == 'GET':
            return True
         if request.user and request.user.groups.filter(name="IsAdmin") or request.user.is_staff:
            return True
         return False