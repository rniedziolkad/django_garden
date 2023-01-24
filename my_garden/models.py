import datetime

from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    choices_list = (("low", "skąpe"),
                    ("medium", "umiarkowane"),
                    ("high", "obfite"),
                    ("very_high", "bardzo obfite"))

    name = models.CharField(max_length=255)
    image_url = models.URLField()
    watering_level = models.CharField(max_length=32, choices= choices_list)
    watering_period = models.DurationField()

    def __str__(self):
        return self.name


class UserPlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    last_watering = models.DateTimeField(default=datetime.datetime.now)
    location = models.TextField(default="", blank=True)
    next_watering = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user)+" -> "+str(self.plant)

