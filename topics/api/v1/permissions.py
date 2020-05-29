"""
API V1: Topics Permissions
"""
###
# Libraries
###
from rest_framework import permissions

###
# Permissions
###


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
