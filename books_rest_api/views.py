from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BucketlistSerializer, UserSerializer
from .models import BookList
from django.contrib.auth.models import User


class CreateView(generics.ListCreateAPIView):
    """Handle Get or Post Requests"""
    queryset = BookList.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Create a new book."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Get, Update or Delete Requests."""

    queryset = BookList.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
class GetAllBooks(generics.ListAPIView):
    """List of all books."""

    queryset = BookList.objects.all()
    serializer_class = BucketlistSerializer

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,IsOwner)

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,IsOwner)
