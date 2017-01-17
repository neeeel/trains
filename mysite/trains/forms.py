from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_sdf = forms.CharField(label='Your sdf', max_length=100)