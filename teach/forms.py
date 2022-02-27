from dataclasses import fields
import imp
from django import forms
from django.forms import TextInput, MultipleChoiceField
from .models import *

class AddTenant(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ("tname","tmarital_status","tyear_in","troom_type")
        widgets={
            'resident': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                
            }),
        }