from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create User
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        # Create a Blog Post
        test_post = Post.objects.create(
            author=testuser1, title='Test blog title', body='Test blog body content......')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Test blog title')
        self.assertEqual(body, 'Test blog body content......')
