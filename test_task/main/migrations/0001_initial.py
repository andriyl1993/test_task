# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('is_private', models.BooleanField(default=False, verbose_name='\u0427\u0438 \u043f\u0440\u0438\u0432\u0430\u0442\u0438\u043d\u0438\u0439 \u0434\u043e\u043c\u0435\u043d?')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043c\u0435\u043d',
                'verbose_name_plural': '\u0414\u043e\u043c\u0435\u043d\u0438',
            },
        ),
    ]
