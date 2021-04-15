from django.urls import path

from . import views

urlpatterns = [
    path('your-name/', views.get_name, name='get_name'),
]