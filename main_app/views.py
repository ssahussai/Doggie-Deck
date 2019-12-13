from django.shortcuts import render
from django.http import HttpResponse

# Deine the home view
def home(request):
    return HttpResponse('<h1>Hello Dog Lover!</h1>')

# define about view
def about(request):
    return render(request, 'about.html')