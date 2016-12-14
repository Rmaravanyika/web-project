from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coding_clubs(request):
    return render(request, 'coding_clubs.html')

def events(request):
    return render(request, 'events.html')

def social_impact(request):
    return render(request, 'social_impact.html')

def mentor(request):
    return render(request, 'mentor.html')

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')
# Create your views here.
