from django import forms

class DrivesAddForm(forms.Form):
    name = forms.CharField(label='Drive name', max_length=50)
    description = forms.CharField(label='Drive description', max_length=180)
