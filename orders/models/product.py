# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Product(models.Model):
    camp = models.ForeignKey('Camp', related_name='products')
    abrasive = models.ForeignKey('Abrasive', related_name='products')
    color = models.ForeignKey('Color', related_name='products')
    order = models.ForeignKey('Order', related_name='products')
    sizeX = models.DecimalField(max_digits=5, decimal_places=2)
    sizeY = models.DecimalField(max_digits=5, decimal_places=2)
    sizeZ = models.DecimalField(max_digits=5, decimal_places=2)
    STATUS_CHOICES = (
        (0.34, '0.34'),
        (0.44, '0.44'),
        (0.32, '0.32'),
    )
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
        return self.camp.name + ' ' + self.abrasive.name + ' ' + self.color.name + ' ' + self.sizeX + 'x' + self.sizeY + 'x' + self.sizeZ + " " + self.color.name
