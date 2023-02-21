# Generated by Django 4.1.6 on 2023-02-19 07:44

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0006_alter_profile_coverimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover_image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='coverimg',
            field=models.ImageField(default='bg.jpeg', upload_to='cover_images'),
        ),
    ]