from django import forms

class AbiForm(forms.Form):
    file = forms.FileField()
