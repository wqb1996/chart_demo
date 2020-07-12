from django.http import HttpResponse
from django.shortcuts import render
from .models import Patent
# Create your views here.

def index(request):

    patents = Patent.objects.all()
    for patent in patents:
        print(patent.pa.all())

    return HttpResponse('OK')