# Generated by Django 3.0 on 2020-03-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200316_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
