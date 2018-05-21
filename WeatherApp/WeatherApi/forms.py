from django import forms 

class LocationSearchForm (forms.Form):
    location = forms.CharField(maxlength=100)