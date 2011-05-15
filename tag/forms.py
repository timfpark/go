from django import forms

class TagEditForm(forms.Form):
    url = forms.CharField(required=True)
