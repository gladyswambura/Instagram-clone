# Generated by Django 4.0.5 on 2022-06-05 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0003_remove_post_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_name',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
