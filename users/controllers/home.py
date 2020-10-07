import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'home/index.html', {"today":today})
