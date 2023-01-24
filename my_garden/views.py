from django.shortcuts import render, HttpResponse
from .models import UserPlant
from django.contrib.auth.decorators import login_required
from .forms import UserPlantForm


@login_required()
def index(request):
    my_plants = UserPlant.objects.filter(user=request.user)
    return render(request, template_name='my_garden/mygarden.html', context={'my_plants': my_plants})


@login_required()
def add_plant(request):
    if request.method == 'POST':
        form = UserPlantForm(request.POST)
        if form.is_valid():
            u_plant = form.save(commit=False)
            u_plant.user = request.user
            u_plant.save()

    form = UserPlantForm()
    return render(request, template_name='my_garden/add_plant.html', context={'form': form})

