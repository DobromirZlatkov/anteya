# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_for_one',
            field=models.DecimalField(max_digits=10, decimal_places=2, choices=[(Decimal('0.340000000000000024424906541753443889319896697998046875'), 0.34), (Decimal('0.440000000000000002220446049250313080847263336181640625'), 0.44), (Decimal('0.320000000000000006661338147750939242541790008544921875'), 0.32)]),
        ),
    ]
