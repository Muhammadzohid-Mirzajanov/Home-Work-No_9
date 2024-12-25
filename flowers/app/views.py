from django.shortcuts import render,get_object_or_404,redirect
from .models import Type,Flower
from .models import Type, Flower
from .forms import FlowerForm, TypeForm

def all_flowers(request):
    flowers = Flower.objects.all()
    return render(request,'all_flowers.html',{'flowers':flowers})

def flowers_by_type(request,type_id):
    type_obj = get_object_or_404(Type,id = type_id)
    flowers = type_obj.flowers.all()
    return render(request,'flowers_by_type.html',{'flowers' : flowers})

def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flower_detail.html', {'flower': flower})


def add_flower(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_flowers')
    else:
        form = FlowerForm()
    return render(request, 'add_flower.html', {'form': form})

# Yangi tur qo'shish
def add_type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_flowers')
    else:
        form = TypeForm()
    return render(request, 'add_type.html', {'form': form})