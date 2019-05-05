# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 18:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feature_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
                ('score', models.IntegerField()),
                ('time', models.DateField(default=datetime.datetime(2019, 5, 5, 18, 28, 30, 303696, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('time', models.DateField(default=datetime.datetime(2019, 5, 5, 18, 28, 30, 302114, tzinfo=utc))),
                ('status', models.IntegerField(choices=[(1, 'SAFE'), (0, 'NEUTRAL'), (-1, 'UNSAFE')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='feature_score',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Website'),
        ),
    ]
