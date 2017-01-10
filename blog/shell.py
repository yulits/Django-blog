import datetime
from django.utils import timezone
from blog.models import Post
from django.contrib.auth.models import User

time = timezone.now() + datetime.timedelta(days=30)
user = User.objects.get(username = 'yuliya')
Post.objects.create(title='title %s' % time, slug='slug_%s' % time, author=user, body='body', publish=time, created=time, updated=time, status='published')
