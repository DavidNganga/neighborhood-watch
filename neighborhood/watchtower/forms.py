from .models import User,Neighborhood
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['name','neighborhood','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields=['name','location','event']
        exclude =["no_occupants"]
