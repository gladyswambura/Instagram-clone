from django.contrib import admin
from .models import Profile, Post, Comment, Notification, Follow, Stream, tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(tags)