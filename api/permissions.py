from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthenticatedFullPermission(BasePermission):
    def has_permission(self, request, view):
        # print('has_permission:', view.action)
        if request.method in SAFE_METHODS:
            return True
        # TODO: 严格权限开控制
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # print('has_object_permission:', view.action)
        if request.method in SAFE_METHODS:
            return True
        # TODO: 严格权限开控制
        return request.user.is_authenticated