from django import forms
from .models import UserPlant
from django.forms import DateTimeInput


class UserPlantForm(forms.ModelForm):
    class Meta:
        model = UserPlant
        fields = ['plant', 'location']


class ManagePlantForm(forms.ModelForm):
    class Meta:
        model = UserPlant
        fields = ['next_watering']
        widgets = {
            'next_watering': DateTimeInput(attrs={"type": "datetime-local"})
        }
