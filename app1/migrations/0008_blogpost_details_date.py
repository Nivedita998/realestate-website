# Generated by Django 3.0 on 2020-03-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_blogpost_details_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost_details',
            name='date',
            field=models.IntegerField(default=0),
        ),
    ]
