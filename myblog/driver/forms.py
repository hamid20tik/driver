from django import forms
from .models import safar,driver,person

class safarform(forms.ModelForm):
    class Meta:
        model = safar
        fields = ['driver','person','mamoriat','mabda','maghsad','datetime_start']