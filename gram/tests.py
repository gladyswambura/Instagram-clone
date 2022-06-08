from django.test import TestCase
from .models import Comment, Profile, Post
# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        self.first_name = Profile(first_name='gladys')
        self.first_name.save()
        self.profile = Profile(id=12 ,profile='image.jpg', bio='Test profile',
                                    first_name=self.first_name)

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
