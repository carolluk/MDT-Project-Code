# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRICD', '0004_usercodesfit'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercodesfit',
            name='mytoken',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercodesfit',
            name='url',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
