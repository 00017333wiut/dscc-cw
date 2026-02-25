from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category


class HealthCheckTest(TestCase):
    def test_health_check_returns_200(self):
        client = Client()
        response = client.get('/health/')
        self.assertEqual(response.status_code, 200)


class PostListTest(TestCase):
    def test_post_list_returns_200(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')

    def test_post_creation(self):
        post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
        )
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(str(post), 'Test Post')

    def test_post_author(self):
        post = Post.objects.create(
            title='Author Test',
            content='Content',
            author=self.user,
        )
        self.assertEqual(post.author.username, 'testuser')


class AuthTest(TestCase):
    def test_login_page_returns_200(self):
        client = Client()
        response = client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)