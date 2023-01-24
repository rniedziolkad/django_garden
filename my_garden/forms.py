from django import forms
from .models import UserPlant


class UserPlantForm(forms.ModelForm):
    class Meta:
        model = UserPlant
        fields = ['plant', 'location']
