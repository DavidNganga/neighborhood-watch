from .models import User
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude=[]
