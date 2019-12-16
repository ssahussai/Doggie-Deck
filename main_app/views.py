from django.shortcuts import render
from django.http import HttpResponse

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age 

dogs = [
    Dog('Rufus', 'pomeranian', 'sweet little dog', 3),
    Dog('Lia', 'poodle', 'full of energy and easy to train', 0),
    Dog('Tommy', 'beagle', 'curious and very sweet', 4)
]



# Deine the home view
def home(request):
    return HttpResponse('<h1>Hello Dog Lover!</h1>')

# define about view
def about(request):
    return render(request, 'about.html')

# adds new view 
def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })