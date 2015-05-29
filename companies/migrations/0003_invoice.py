# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20150529_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('url', models.URLField()),
                ('status', models.CharField(default=b'unpayed', max_length=100, verbose_name=b'Status', choices=[(b'unpayed', '\u041f\u043b\u0430\u0442\u0435\u043d\u0430'), (b'payed', '\u041d\u0435\u043f\u043b\u0430\u0442\u0435\u043d\u0430')])),
                ('is_successfully_created', models.BooleanField(default=False)),
                ('failure_reason', models.CharField(default=None, max_length=400, null=True, blank=True)),
                ('inv_rest_id', models.IntegerField(default=None, null=True, blank=True)),
                ('company', models.ForeignKey(related_name='invoices', to='companies.Company')),
            ],
        ),
    ]
