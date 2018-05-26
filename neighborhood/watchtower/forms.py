from .models import Profile,Neighborhood
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','neighborhood','email']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields=['name','location','event']
        exclude =['no_occupants']
