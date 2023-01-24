from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import UserPlant
from django.contrib.auth.decorators import login_required
from .forms import UserPlantForm, ManagePlantForm
from django.core.exceptions import PermissionDenied


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
