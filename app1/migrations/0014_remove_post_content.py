# Generated by Django 3.0 on 2020-03-19 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
