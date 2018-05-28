from .models import Profile,Neighborhood,Establishment
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','neighborhood','email']
        exclude =['user']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields=['name','location','event_details','user']
        exclude =['no_occupants']

class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields=['name','email','neighborhood','user','description']
        exclude =[]
