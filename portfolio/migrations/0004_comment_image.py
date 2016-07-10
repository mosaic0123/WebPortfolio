# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20151018_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
