from django.urls import path
from .views import ItemListView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('itemlist/',views.list),
    path('search/',views.search),
]