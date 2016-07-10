# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('parent', models.IntegerField(null=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='project',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
