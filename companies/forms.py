# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from . import models


class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = ['company_name', 'bulstat', 'mol', 'town', 'address', 'recipient', 'bank_name', 'bank_iban', 'bank_bic']

        widgets = {
            'company_name': forms.TextInput(
                attrs={'required': True, 'placeholder': 'Име на фирмата*', 'class': 'form-control',}
            ),
            'bulstat': forms.TextInput(
                attrs={'required': True, 'placeholder': 'Булстат*', 'class': 'form-control',}
            ),
            'mol': forms.TextInput(
                attrs={'required': True, 'placeholder': 'Мол*', 'class': 'form-control',}
            ),
            'town': forms.TextInput(
                attrs={'required': True, 'placeholder': 'Град*', 'class': 'form-control',}
            ),
            'address': forms.TextInput(
                attrs={'required': True, 'placeholder': 'Адрес*', 'class': 'form-control',}
            ),
            'recipient': forms.TextInput(
                attrs={'required': True, 'placeholder': 'Получател на фактурата', 'class': 'form-control',}
            ),
            'bank_name': forms.TextInput(
                attrs={'required': False, 'placeholder': 'Банка', 'class': 'form-control',}
            ),
            'bank_iban': forms.TextInput(
                attrs={'required': False, 'placeholder': 'Банка ИБАН', 'class': 'form-control',}
            ),
            'bank_bic': forms.TextInput(
                attrs={'required': False, 'placeholder': 'Банка БИК', 'class': 'form-control',}
            ),
        }

