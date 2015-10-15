# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('size', models.CharField(max_length=20)),
                ('file_type', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('version', models.CharField(max_length=20)),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(to='portfolio.Project'),
        ),
    ]
