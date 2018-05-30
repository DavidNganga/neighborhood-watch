from .models import Profile,Neighborhood,Establishment,Post
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','neighborhood','email','profile_photo']
        exclude =['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['name','location','event_details','user']
        exclude =[]

class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields=['name','email','neighborhood','user','description']
        exclude =[]

class CreateNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields=['name','location']
        exclude =['no_occupants','event_details','user']
