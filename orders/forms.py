# -*- coding: utf-8 -*-
from django import forms

from django.forms.formsets import formset_factory, BaseFormSet

from . import models


class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ['date']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        exclude = ['order']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['sizeX'].widget.attrs['class'] = 'form-control'
        self.fields['sizeX'].decimal_places = 2
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

ProductFormSet = formset_factory(ProductForm, formset=RequiredFormSet)

