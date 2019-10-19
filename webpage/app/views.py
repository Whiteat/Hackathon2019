from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from app.models import *


# Create your views here.

def index(request):
    return render_to_response('index.html')

def greenhouses(request):
    context = {
        'greenhouses': Greenhouse.objects.all()
    }
    return render(request, 'greenhouses.html', context)

def greenhouse(request, id):
    greenhouse = Greenhouse.objects.get(id=id)
    certifications = Certification.objects.filter(greenhouse = greenhouse.id).values()
    products = Unit.objects.filter(greenhouse = greenhouse.id).values()
    print(certifications)
    context = {
        'greenhouse': greenhouse,
        'certifications': certifications,
        'products': products,
    }
    return render(request, 'greenhouse.html', context)
