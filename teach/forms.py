from dataclasses import fields
import imp
from django import forms
from django.forms import TextInput, MultipleChoiceField
from django.forms import widgets
from .models import *

class AddTenant(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ("tname","tmarital_status","tyear_in","troom_type")
        widget={
            'resident': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                
            }),
        }