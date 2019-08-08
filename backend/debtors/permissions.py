from rest_framework.permissions import BasePermission


class CreatedByCurrentAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.is_created_by_admin(request.user)