from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import data
# Create your views here.


def view_data (request):
    #data_objects = data.objects.all().order_by('timestamp').distinct('device_id')\
    data_objects = data.objects.all().order_by('device_id', '-timestamp').distinct('device_id') #FINDS ALL LATEST DATA OF EVERY UNIQUE DEVICE ID
    return render (request, 'main.html', {'data': data_objects})

def insert_data (request):
    if request.method == "POST":
        newitem = data (id = request.POST.get('id'), device_id = request.POST.get('device_id'), latitude = request.POST.get('latitude'), longitude = request.POST.get('longitude'), temp = request.POST.get('temp'), loc_humidity = request.POST.get('loc_humidity'), sm1 = request.POST.get('sm1'), sm2 = request.POST.get('sm2'), sm3 = request.POST.get('sm3'), sm4 = request.POST.get('sm4'), sm5 = request.POST.get('sm5'), sm6 = request.POST.get('sm6'), sm7 = request.POST.get('sm7'), sm8 = request.POST.get('sm8'), amb_ll = request.POST.get('amb_ll'), timestamp = request.POST.get('timestamp'))
        newitem.save()
        return HttpResponseRedirect (reverse('webfront:view_data'))
    
    else:
        return render (request, 'form.html')

def edit (request, id):
    if request.method == "POST":
        newitem = data (id = request.POST.get('id'), device_id = request.POST.get('device_id'), latitude = request.POST.get('latitude'), longitude = request.POST.get('longitude'), temp = request.POST.get('temp'), loc_humidity = request.POST.get('loc_humidity'), sm1 = request.POST.get('sm1'), sm2 = request.POST.get('sm2'), sm3 = request.POST.get('sm3'), sm4 = request.POST.get('sm4'), sm5 = request.POST.get('sm5'), sm6 = request.POST.get('sm6'), sm7 = request.POST.get('sm7'), sm8 = request.POST.get('sm8'), amb_ll = request.POST.get('amb_ll'), timestamp = request.POST.get('timestamp'))
        data_item = data.objects.get(id=id)
        data_item = newitem
        data_item.save()
        return HttpResponseRedirect (reverse('webfront:view_data'))
    
    else:
        data_item = data.objects.get(id=id)
        return render (request, 'edit.html', {'data_item': data_item})

def delete (request, id):
    data_item = data.objects.get(id=id)
    data_item.delete()
    return HttpResponseRedirect (reverse('webfront:view_data'))

def history (request, id):
    data_objects = data.objects.all().filter(device_id=id)
    return render (request, 'devicedata.html', {'data': data_objects})