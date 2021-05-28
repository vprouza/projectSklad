from django.shortcuts import render
from django.http import HttpResponse, request
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from items.models import Item
from django.contrib.auth.models import User


class ItemListView(ListView):
    model = Item
    template_name = 'transactions/items_list.html'

@login_required
def index(request):
    output = _("Hello world")
    if request.user.is_authenticated:
        username = request.user.get_full_name()
        #print(request.user)
        output = "logged in as: " + username + "\n" + str(request.user.seller.order_in_progress)
    else:
        output = "not logged in"
    #return HttpResponse(output)
    return render(request, 'content.html')


def list(request):
    result = Item.objects.all()
    site = "Search result"
    context = {'result': result,
    'title' : site}
    return render(request, "content.html", context)


def search(request):
    str = request.GET.get("search",default="")
    result = Item.objects.filter(name__contains=str)
    site = "Search result"
    context = {'result': result,
    'title' : site}
    return render(request, "search.html", context)