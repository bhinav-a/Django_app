from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'John', 'age': 15},
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 15},
        {'name': 'Disha', 'age': 19}
        ]
    
    vegetables = ['Pumpkins' , 'Tomato' , 'Cucumber' , 'Carrot']
    return render (request, 'homepage/index.html' , context = {'page' : 'Django' ,'peoples':peoples})

def about(request):
    context = {'page' : 'About'}
    return render (request, 'homepage/about.html' , context)

def contact(request):
    context = {'page' :'Contact'}
    return render (request, 'homepage/contact.html' , context)

def success_page(request):
    return HttpResponse("<h1>Success page</h1>")