from django import forms
from .models import safar,driver,person

class safarform(forms.ModelForm):
    driver = forms.Select(attrs={'class': 'form-control',
               })

    mabda = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control',
        }
    ))
    mamoriat = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               }
    ))
    maghsad = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               }
    ))



    class Meta:
        model = safar
        fields = ['driver','person','mamoriat','mabda','maghsad']