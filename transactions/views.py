from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from items.models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'transactions/items_list.html'

@login_required
def index(request):
    output = _("Hello world")
    if request.user.is_authenticated:
        username = request.user.get_full_name()
        #print(request.user)
        output = "logged in as: " + username
    else:
        output = "not logged in"
    return HttpResponse(output)