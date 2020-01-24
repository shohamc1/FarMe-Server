from django.urls import path
from . import views

app_name = "varset"

urlpatterns = [
    path('', views.main_view, name='var_view'),
    path('add', views.var_add, name="varadd"),
    path('varchange/<int:id>', views.var_edit, name='varchange'),
    path('vardelete/<int:id>', views.var_delete, name='vardelete'),
]