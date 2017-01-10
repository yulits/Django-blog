import datetime
from django.test import TestCase
from django.utils import timezone
from blog.models import Post
from django.contrib.auth.models import User

def create_post(days, user, title='title', slug='slug', body='body'):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    
    return Post.objects.create(title=title, slug=slug, author=user, body=body,
                               publish=time, created=time, updated=time, status='published')

class PostTests(TestCase):

    def test_publish_in_future(self):
        """
        future_post.publish < timezone.now() should return False for questions whose
        publish is in the future.
        """
        user = User.objects.create_user('diana', 'diana@thebeatles.com', 'dianapassword')
        future_post = create_post(30, user)
        self.assertEqual(future_post.publish < timezone.now(), False)
        
    def test_publish_in_past(self):
        """
        future_post.publish < timezone.now() should return True for questions whose
        publish is in the past.
        """
        user = User.objects.create_user('diana', 'diana@thebeatles.com', 'dianapassword')
        future_post = create_post(-30, user)
        self.assertEqual(future_post.publish < timezone.now(), True)
        
    def test_double_slug(self):
        user = User.objects.create_user('diana', 'diana@thebeatles.com', 'dianapassword')
        create_post(0, user, slug='myslug')
        create_post(0, user, slug='myslug')
        self.assertEqual(len(Post.objects.filter(slug='myslug')) > 1, True)
        