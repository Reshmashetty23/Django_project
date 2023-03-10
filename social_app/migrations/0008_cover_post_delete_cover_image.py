# Generated by Django 4.1.6 on 2023-02-19 11:43

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0007_cover_image_alter_profile_coverimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover_Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user1', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='post_images')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Cover_image',
        ),
    ]
