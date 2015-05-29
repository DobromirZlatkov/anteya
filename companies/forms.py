# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from . import models


class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = ['company_name']
        widgets = {
            'company_name': forms.TextInput(
                attrs={'required': True, 'placeholder': 'Име на фирмата*', 'class': 'form-control', 'label':'Име'}
            ),
        }
        # widgets = {
        #   'website': forms.TextInput()
        # }

