from ca.models import Donateur
from django import forms

class DonateurCreateForm(forms.ModelForm):
    class Meta:
        model = Donateur
        fields ='__all__'