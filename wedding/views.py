from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def base_url(request):
    return render(request, 'wedding/wrapper.html')
