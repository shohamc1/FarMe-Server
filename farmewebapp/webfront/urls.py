from django.urls import path
from . import views

app_name = "webfront"

urlpatterns = [
    path('', views.view_data, name='view_data'),
    path('add/', views.insert_data, name="insert_data"),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')
]