# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default=datetime.datetime(2015, 5, 29, 7, 47, 18, 713995, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='bank_bic',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='bank_iban',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='bank_name',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='bulstat',
            field=models.CharField(default='bulstat', max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='mol',
            field=models.CharField(default=datetime.datetime(2015, 5, 29, 7, 47, 32, 266822, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='recipient',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='town',
            field=models.CharField(default=b'Sofia', max_length=200),
        ),
    ]
