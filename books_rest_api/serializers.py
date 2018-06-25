from rest_framework import serializers
from .models import BookList
from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = BookList
        fields = ('id', 'name','price','author','genre', 'owner','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    booklists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=BookList.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'booklists')
