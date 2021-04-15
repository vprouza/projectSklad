from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


def index(request):
    output = _("Hello world")
    return HttpResponse(output)