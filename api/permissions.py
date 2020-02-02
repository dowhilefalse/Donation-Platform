from rest_framework.permissions import BasePermission


class AuthenticatedFullPermission(BasePermission):
    def has_permission(self, request, view):
        print('has_permission:', view.action)
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        print('has_object_permission:', view.action)
        return request.user.is_authenticated