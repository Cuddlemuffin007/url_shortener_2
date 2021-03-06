# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 19:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('shortened', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_accessed', models.DateTimeField(null=True)),
                ('access_count', models.IntegerField(default=0)),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='short_url_app.Bookmark')),
            ],
        ),
    ]
