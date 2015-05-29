# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from utils import datetime_utils


class Invoice(models.Model):
    STATUSES = (
        ('unpayed', u'Платена'),
        ('payed', u'Неплатена'),
    )
    company = models.ForeignKey('Company', related_name='invoices')
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.URLField()
    status = models.CharField('Status', max_length=100, choices=STATUSES, default='unpayed')
    is_successfully_created = models.BooleanField(default=False)
    failure_reason = models.CharField(max_length=400, blank=True, null=True, default=None)
    inv_rest_id = models.IntegerField(blank=True, null=True, default=None)

    @property
    def time_period(self):
        return datetime_utils.string_from_date(self.from_date, '%d.%m.%Y') + '--' + datetime_utils.string_from_date(self.to_date, '%d.%m.%Y')
