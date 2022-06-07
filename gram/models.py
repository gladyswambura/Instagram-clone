import profile
from django.db import models
from  tinymce.models import HTMLField
import datetime as dt
# from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User         # for profile model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_picture", default="default.jpg")
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    # favourite = models.ManyToManyField(Post, blank=True)


    def __str__(self):
        return f'{self.user.username} -profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    @property
    def saved_followers(self):
        return self.saved_followers.count()   

    @property
    def saved_following(self):
        return self.following.count() 


    @property
    def follows(self):
        return [follow.followers for follow in self.following.all()]

    @property
    def following(self):
        return self.saved_followers.all()

    @classmethod
    def search_profiles(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains = search_term).all()
        return profiles

    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    picture = models.ImageField(upload_to="user_directory_path", verbose_name="Picture")
    caption = models.TextField(max_length=1000, null=True )
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=60, default="", blank=True)
    likes = models.PositiveIntegerField(default=0)

    def save_picture(self):
     self.save()

    @classmethod
    def get_posts(cls):
        posts =Post.objects.all()
        return posts

    def __str__(self):
       return str(self.caption)

    @classmethod
    def display_posts(cls):
        posts = cls.objects.all().order_by('-posted_at')
        return posts
    # uploading user files to a specific directory
    def user_directory_path(instance, filename):
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    def delete_post(self):
        self.delete()

    def __str__(self):
        return "%s post" % self.post_name

# class Likes(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post_likes = models.ForeignKey(Post, on_delete=models.CASCADE)

#     def user_liked_post(sender, instance, *args, **kwargs):
#         post_likes = instance
#         post =  post_likes.post
#         sender =  post_likes.user
#         notify = Notification(post=post, sender=sender, user=post.user)
#         notify.save()

#     def user_unliked_post(sender, instance, *args, **kwargs):
#         post_likes = instance
#         post =  post_likes.post
#         sender =  post_likes.user
#         notify = Notification.objects.filter(post=post, sender=sender, notification_types=1)
#         notify.delete()


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def user_follow(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following
        notify = Notification(sender=sender, user=following, notification_types=3)
        notify.save()

    def user_unfollow(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following
        notify = Notification.objects.filter(sender=sender, user=following, notification_types=3)
        notify.delete()

class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)

        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
            stream.save()
    
class Comment(models.Model):
    image = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment

class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))

    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="notification_post", null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_from_user" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_to_user" )
    notification_types = models.IntegerField(choices=NOTIFICATION_TYPES, null=True, blank=True)
    text_preview = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name