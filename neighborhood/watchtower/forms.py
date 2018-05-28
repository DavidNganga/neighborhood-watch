from .models import Profile,Neighborhood,Business
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','neighborhood','email']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields=['name','location','event_details']
        exclude =['no_occupants']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','email','neighborhood','user','description']
        exclude =[]
