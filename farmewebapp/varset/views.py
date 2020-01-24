from django.shortcuts import render
from .models import var_data
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def main_view (request):
    data_objects = var_data.objects.all()
    return render (request, 'varmain.html', {'data': data_objects})

def var_edit(request, id):
    if request.method == "POST":
        newitem = var_data (id = id, device_id = request.POST.get('device_id'), latitude = request.POST.get('latitude'), longitude = request.POST.get('longitude'))
        print (newitem.latitude)
        data_item = var_data.objects.get(id = id)
        data_item = newitem
        data_item.save()
        return HttpResponseRedirect (reverse('varset:var_view'))
    
    else:
        data_object = var_data.objects.get(id = id)
        return render (request, 'varedit.html', {'data_item': data_object})

def var_delete(request, id):
    data_item = var_data.objects.get(id=id)
    data_item.delete()
    return HttpResponseRedirect (reverse('varset:var_view'))

def var_add (request):
    if request.method == "POST":
        newitem = var_data (id = request.POST.get('device_id'), device_id = request.POST.get('device_id'), latitude = request.POST.get('latitude'), longitude = request.POST.get('longitude'))
        newitem.save()
        return HttpResponseRedirect (reverse('varset:var_view'))
    
    else:
        return render (request, 'varadd.html')