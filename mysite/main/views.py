from django.shortcuts import render
from .models import *

def index(request):
    brands = Brand.objects.raw('SELECT * FROM main_brand')
    return render(request, 'main/base.html', context={'brands': brands})

