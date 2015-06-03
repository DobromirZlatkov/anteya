# -*- coding: utf-8 -*-
from django.db import models
from decimal import Decimal
TWOPLACES = Decimal(10) ** -2

# Create your models here.
class Product(models.Model):
    camp = models.ForeignKey('Camp', related_name='products')
    abrasive = models.ForeignKey('Abrasive', related_name='products')
    color = models.ForeignKey('Color', related_name='products')
    order = models.ForeignKey('Order', related_name='products')
    sizeX = models.DecimalField(max_digits=5, decimal_places=2)
    sizeY = models.DecimalField(max_digits=5, decimal_places=2)
    sizeZ = models.DecimalField(max_digits=5, decimal_places=2)
    STATUS_CHOICES = [
        [Decimal(0.34).quantize(TWOPLACES), '0.34'],
        [Decimal(0.44).quantize(TWOPLACES), '0.44'],
        [Decimal(0.32).quantize(TWOPLACES), '0.32'],
    ]
    price_for_one = models.DecimalField(max_digits=10, decimal_places=2, choices=STATUS_CHOICES)
    quantity = models.IntegerField()
    TYPES = [
        ['schlei', u'Шлайфане'],
        ['cutting', u'Рязане'],
        ['schlei_and_cutting', u'Рязане и шлайфане'],
    ]
    action = models.CharField(
        max_length=250,
        choices=TYPES
    )

    def __unicode__(self):
        return self.camp.name + ' ' + self.abrasive.name + ' ' + str(self.sizeX) + 'x' + str(self.sizeY) + 'x' + str(self.sizeZ) + " " + self.color.name

    @property
    def total_amount(self):
        return self.price_for_one * self.quantity
