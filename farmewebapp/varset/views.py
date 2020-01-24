from django.shortcuts import render
from .models import var_data
# Create your views here.

def main_view (request):
    data_objects = var_data.objects.all()
    return render (request, 'main.html', {'data': data_objects})
