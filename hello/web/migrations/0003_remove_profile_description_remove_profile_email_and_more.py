# Generated by Django 4.0.3 on 2022-03-30 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_petphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]
