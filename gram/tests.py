from django.test import TestCase
from .models import Comment, Profile, Image
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username='hezron')
        self.user.save()
        self.profile = Profile(id=12 ,profile='image.jpg', bio='Test profile',
                                    user=self.user)
