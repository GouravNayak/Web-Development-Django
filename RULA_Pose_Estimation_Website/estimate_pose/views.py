from django.shortcuts import render
from django.http import HttpResponse, Http404


def home(request):
    # return HttpResponse('<p>home</p>')
    return render(request, 'home.html')
