# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0003_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='UserIdfk',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='gameURL',
            field=models.URLField(default='', max_length=50),
        ),
    ]