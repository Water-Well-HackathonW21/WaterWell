from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {'first_name': 'Max', 'last_name': 'Melendez'}
    return render(request, 'about.html', context)
