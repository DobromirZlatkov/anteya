# -*- coding: utf-8 -*-
from django import forms

from django.forms.formsets import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

from decimal import Decimal

from . import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        exclude = ['order']

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            kwargs['instance'].price_retail = kwargs['instance'].sizeX.quantize(Decimal('0.01'))
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['sizeX'].widget.attrs['class'] = 'form-control'
        self.fields['sizeX'].decimal_places = 2
        self.fields['sizeX'].min_value = 0
        self.fields['sizeY'].widget.attrs['class'] = 'form-control'
        self.fields['sizeY'].decimal_places = 2
        self.fields['sizeZ'].widget.attrs['class'] = 'form-control'
        self.fields['sizeZ'].decimal_places = 2
        self.fields['camp'].widget.attrs['class'] = 'form-control'
        self.fields['abrasive'].widget.attrs['class'] = 'form-control'
        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['price_for_one'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['action'].widget.attrs['class'] = 'form-control'

ProductFormSet = formset_factory(ProductForm)

