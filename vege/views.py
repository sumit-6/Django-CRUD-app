from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def add_recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )
        return redirect('/')
    context = {'page': 'add_recipe'}
    return render(request, 'add_recipe.html', context)
    
def recipes(request):
    queryset = Recipe.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {"recipes": queryset, 'page': 'recipes'}
    return render(request, 'recipes.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        return redirect('/')
    context = {'recipe': queryset, 'page': 'update recipes'}
    return render(request, 'update_recipe.html', context)
