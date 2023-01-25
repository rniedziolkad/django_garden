from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import UserPlant, Plant
from django.contrib.auth.decorators import login_required
from .forms import UserPlantForm, ManagePlantForm, PlantForm
from django.core.exceptions import PermissionDenied


@login_required()
def index(request):
    my_plants = UserPlant.objects.filter(user=request.user)
    return render(request, template_name='my_garden/mygarden.html', context={'my_plants': my_plants})


@login_required()
def add_plant(request):
    if request.method == 'POST':
        form = UserPlantForm(request.user, request.POST)
        if form.is_valid():
            u_plant = form.save(commit=False)
            u_plant.user = request.user
            u_plant.save()

    form = UserPlantForm(request.user)
    return render(request, template_name='my_garden/add_plant.html', context={'form': form})


@login_required()
def manage_plant(request, pk):
    u_plant = get_object_or_404(UserPlant, pk=pk)
    if u_plant.user != request.user:
        raise PermissionDenied()
    if request.method == 'POST':
        form = ManagePlantForm(request.POST, instance=u_plant)
        if form.is_valid():
            form.save()
    else:
        form = ManagePlantForm(instance=u_plant)
    return render(request, template_name='my_garden/manage_plant.html', context={'form': form, 'u_plant': u_plant})


@login_required()
def plant_list(request):
    plants = Plant.objects.filter(added_by=None)
    user_plants = Plant.objects.filter(added_by=request.user)
    return render(request, template_name='my_garden/plant_list.html',
                  context={'plants': plants, 'user_plants': user_plants})


@login_required()
def add_plant_list(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.added_by = request.user
            plant.save()

    form = PlantForm()
    return render(request, template_name='my_garden/add_plant_list.html', context={'form': form})


@login_required()
def edit_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if plant.added_by != request.user:
        raise PermissionDenied()
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
    else:
        form = PlantForm(instance=plant)
    return render(request, template_name='my_garden/edit_plant_list.html', context={'form': form, 'plant': plant})
