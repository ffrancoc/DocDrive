from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password1')

class ArchiveForm(forms.ModelForm):    
    class Meta:
        model = models.Archive
        fields = ('file', 'title')
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.png,.jpg,.jpeg,.pdf'})
        }