from django import forms 

class LocationSearchForm (forms.Form):
    location = forms.CharField(label='search',max_length=100)