# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20191105_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default='media/article/first.jpg', upload_to='media/article'),
            preserve_default=False,
        ),
    ]