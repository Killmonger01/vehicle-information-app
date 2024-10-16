from .models import Car
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CarForm
def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})


@login_required
def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.author = request.user
            comment.save()
            return redirect('car:car_detail', car_id=car.id)
    form = CommentForm()
    is_owner = car.owner == request.user
    comments = car.comments.all()
    return render(request, 'car_detail.html', {'car': car, 'form': form, 'comments': comments, 'is_owner': is_owner})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car:index')
    form = CarForm()
    
    return render(request, 'add_car.html', {'form': form})


@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if car.owner != request.user:
        return redirect('car:index')

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car:car_detail', car_id=car.id)
    else:
        form = CarForm(instance=car)

    return render(request, 'edit_car.html', {'form': form, 'car': car})


@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.user == car.owner:
        car.delete()
        return redirect('car:index')
    return redirect('car:index')



