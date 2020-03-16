# Generated by Django 3.0 on 2020-03-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='hometype',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pricepersquarefit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail1',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail2',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
