from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display_view(request):
    print(10/0)
    return HttpResponse('<h1>Good Evening</h1>')
