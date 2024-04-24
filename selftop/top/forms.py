from django import forms

class Upload_form(forms.Form):
    file = forms.FileField()