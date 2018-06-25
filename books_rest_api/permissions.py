from rest_framework.permissions import BasePermission
from .models import BookList

class IsOwner(BasePermission):
    """Custom permission class to allow only booklist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the booklist owner."""
        if isinstance(obj, BookList):
            return obj.owner == request.user
        return obj.owner == request.user