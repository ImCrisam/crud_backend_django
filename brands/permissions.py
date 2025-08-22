from rest_framework import permissions
from django.conf import settings


class HeaderNumberPermission(permissions.BasePermission):
    """Allow read-only requests for everyone. For write requests require a
    numeric X-CLIENT-ID header matching settings.FAKE_CLIENT_ID.
    """

    def has_permission(self, request, view):
        # safe methods allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        header = request.META.get('HTTP_X_CLIENT_ID')
        if not header:
            return False

        # compare as strings to keep it simple
        return str(header) == str(getattr(settings, 'FAKE_CLIENT_ID', '42'))
