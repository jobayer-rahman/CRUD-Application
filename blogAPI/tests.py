from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author


class AuthorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            'first_name': 'test',
            'last_name': 'test',
            'phone_number': '+8801367970660',
            'email': 'test@gmail.com'
        }
        self.author = Author.objects.create(
            first_name='Jobayer',
            last_name='Rahman',
            phone_number='+8801538553160',
            email='test@gmail.com'
        )

    def test_get_all_authors(self):
        response = self.client.get('/author/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        response = self.client.post('/author/', self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_author_details(self):
        response = self.client.get(f'/author/{self.author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_author(self):
        data = {
            'first_name': 'Updated',
            'last_name': 'Author',
            'phone_number': '333333333333',
            'email': 'example@gmail.com'
        }
        response = self.client.put(f'/author/{self.author.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_author(self):
        response = self.client.delete(f'/author/{self.author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

