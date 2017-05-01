# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('bag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_auth.Bag')),
            ],
        ),
    ]
