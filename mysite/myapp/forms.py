# myapp/forms.py
from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label="Enter Text", max_length=100)
