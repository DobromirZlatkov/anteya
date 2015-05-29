# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abrasive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('company', models.ForeignKey(related_name='orders', to='companies.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sizeX', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sizeY', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sizeZ', models.DecimalField(max_digits=5, decimal_places=2)),
                ('price_for_one', models.DecimalField(max_digits=10, decimal_places=2, choices=[(0.34, b'0.34'), (0.44, b'0.44'), (0.32, b'0.32')])),
                ('quantity', models.IntegerField()),
                ('action', models.CharField(max_length=250, choices=[[b'schlei', '\u0428\u043b\u0430\u0439\u0444\u0430\u043d\u0435'], [b'cutting', '\u0420\u044f\u0437\u0430\u043d\u0435'], [b'schlei_and_cutting', '\u0420\u044f\u0437\u0430\u043d\u0435 \u0438 \u0448\u043b\u0430\u0439\u0444\u0430\u043d\u0435']])),
                ('abrasive', models.ForeignKey(related_name='products', to='orders.Abrasive')),
                ('camp', models.ForeignKey(related_name='products', to='orders.Camp')),
                ('color', models.ForeignKey(related_name='products', to='orders.Color')),
                ('order', models.ForeignKey(related_name='products', to='orders.Order')),
            ],
        ),
    ]
