# Generated by Django 2.2.2 on 2019-06-28 21:51

from datetime import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_blog_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='last_update',
            field=models.DateTimeField(default=datetime.now),
        ),
    ]