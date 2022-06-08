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

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >0)
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)
