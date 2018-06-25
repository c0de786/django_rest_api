from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import BookList
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """This class defines the test suite for the booklist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.name = "Write world class code"
        # specify owner of a booklist
        self.booklist = BookList(name=self.name, owner=user)

    def test_model_can_create_a_booklist(self):
        """Test the booklist model can create a booklist."""
        old_count = BookList.objects.count()
        self.booklist.save()
        new_count = BookList.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(self.booklist), self.name)


class ViewsTestCase(TestCase):
    """Test suite for the books_rest_api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Since user model instance is not serializable, use its Id/PK
        self.booklist_data = {'name': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.booklist_data,
            format="json")

    def test_api_can_create_a_booklist(self):
        """Test the books_rest_api has book creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the books_rest_api has user authorization."""
        new_client = APIClient()
        res = new_client.delete('/booklists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_booklist(self):
        """Test the books_rest_api can get a given booklist."""
        booklist = BookList.objects.get(id=1)
        response = self.client.get(
            '/booklists/',
            kwargs={'pk': booklist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, booklist)

    def test_api_can_update_booklist(self):
        """Test the books_rest_api can update a given booklist."""
        booklist = BookList.objects.get()
        change_booklist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': booklist.id}),
            change_booklist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_booklist(self):
        """Test the books_rest_api can delete a booklist."""
        booklist = BookList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': booklist.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)