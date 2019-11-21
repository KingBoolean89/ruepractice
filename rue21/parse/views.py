from django.shortcuts import render
from tablib import Dataset
from .models import *

def index(request):
    return render(request, 'index.html')


  


