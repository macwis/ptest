from rest_framework import permissions
from .models import Blacklist


class BlacklistPermission(permissions.BasePermission):
    """
    Permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META["REMOTE_ADDR"]
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted


class IsBookOwner(permissions.BasePermission):
    """
    Check if user is Book owner or not.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
