from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def add_recipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipes/')
    context = {'page': 'add_recipe'}
    return render(request, 'add_recipe.html', context)
    
def receipes(request):
    queryset = Receipe.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {"receipes": queryset, 'page': 'recipes'}
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('/receipes/')
    context = {'receipe': queryset, 'page': 'update recipes'}
    return render(request, 'update_receipe.html', context)