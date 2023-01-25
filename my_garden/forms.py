from django import forms
from .models import UserPlant, Plant
from django.forms import DateTimeInput
from django.db.models import Q


class UserPlantForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plant'].queryset = Plant.objects.filter(Q(added_by=user) | Q(added_by__isnull=True))

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


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'watering_level', 'watering_period', 'image_url']
