from .models import Profile,Neighborhood,Post
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','neighborhood','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['neighborhood','event']
        exclude =[]
