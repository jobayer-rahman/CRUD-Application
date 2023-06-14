from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Comment, Post


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

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(
            first_name='Jobayer',
            last_name='Rahman',
            phone_number='+8801538553160',
            email='test@gmail.com'
        )
        self.post = Post.objects.create(
            author=self.author,
            title="Test Post test",
            body="This is a test post."
        )

    def test_get_all_posts(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {
            'title': 'New Post',
            'body': 'This is a new post.',
            'author': self.author.id,
        }
        response = self.client.post('/post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_post_details(self):
        response = self.client.get(f'/post/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        data = {
            'title': 'Updated Post',
            'body': 'This post has been updated.',
            'author': self.author.id
        }
        response = self.client.put(f'/post/{self.post.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(f'/post/{self.author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CommentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(
            first_name='Jobayer',
            last_name='Rahman',
            phone_number='+8801538553160',
            email='test@gmail.com'
        )
        self.post = Post.objects.create(
            author=self.author,
            title="Test Post test",
            body="This is a test post."
        )
        self.comment = Comment.objects.create(
            author=self.author,
            post=self.post,
            body="Test comment"
        )

    def test_get_all_comment(self):
        response = self.client.get('/comment/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        data = {
            'body': 'New Comment',
            'post': self.post.id,
            'author': self.author.id,
        }
        response = self.client.post('/comment/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comment_details(self):
        response = self.client.get(f'/comment/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        data = {
            'body': 'Updated Comment',
            'post': self.post.id,
            'author': self.author.id
        }
        response = self.client.put(f'/comment/{self.comment.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        response = self.client.delete(f'/comment/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
