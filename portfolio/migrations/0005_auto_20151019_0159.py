# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_comment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, to='portfolio.Comment'),
        ),
    ]
