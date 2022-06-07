# Generated by Django 4.0.5 on 2022-06-06 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0008_post_likes_delete_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gram.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]