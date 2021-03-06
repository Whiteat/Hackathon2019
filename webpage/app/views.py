from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from app.models import *


# Create your views here.

def index(request):
    return render_to_response('index.html')

def certifications(request):
    context = {
    'certifications': Certification.objects.all(),
    }
    return render(request, 'certifications.html', context)

def certification(request, id):
    context = {
        'certification': Certification.objects.get(id=id),
        }
    return render(request, 'certification.html', context)

def soils(request):
    context = {
    'soils': Soil.objects.all(),
    }
    return render(request, 'soils.html', context)

def soil(request, id):
    context = {
        'soil': Soil.objects.get(id=id),
        }
    return render(request, 'soil.html', context)

def greenhouses(request):
    context = {
        'greenhouses': Greenhouse.objects.all()
    }
    return render(request, 'farms.html', context)

def greenhouse(request, id):
    greenhouse = Greenhouse.objects.get(id=id)
    certifications = Certification.objects.filter(greenhouse = greenhouse.id).values()
    db_products = Unit.objects.filter(greenhouse = greenhouse.id)

    products = []
    for product in db_products:
        products += [{
            'product' : product,
            'recipe': product.plantRecipe,
            }]
        print(product.id)
        print(product.plantRecipe)
        #plantName = PlantRecipe.objects.get(id = product.plantRecipe)
        #print(plantName)

    context = {
        'greenhouse': greenhouse,
        'certifications': certifications,
        'products': products,
    }
    return render(request, 'farm.html', context)

def product(request, id):
    product = Unit.objects.get(id=id)
    print(product.plantRecipe.name)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context)
