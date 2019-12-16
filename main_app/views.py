from django.shortcuts import render
from .models import Dog


# Deine the home view
def home(request):
    return render(request, 'home.html')

# define about view
def about(request):
    return render(request, 'about.html')

# adds new view 
def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })