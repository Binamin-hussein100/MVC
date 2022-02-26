from dataclasses import fields
import imp
from django import forms
from django.forms import TextInput, MultipleChoiceField
from django.forms import widgets
from .models import *

class AddTenant(forms.ModelForm):
    class Meta:
        model = Tenants
        fields = ("tname","tmarital_status","tdate_in","troom_type")