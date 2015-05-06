# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRICD', '0002_tempusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('mycode', models.CharField(max_length=250)),
            ],
        ),
    ]
