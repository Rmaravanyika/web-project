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


class School:
    def __init__(self, key, name, lat, lng):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng

schools = [
    School('hv', 'happy valley elementery', -18.9614993, 24.6564996),
    School('mb', 'mbare', -18.9614993, 24.6564996)
    ]
schools_by_key={school.key:school for school in schools}
#def show_school(request, school_code):
 #   school = schools_by_key.get(school_code)
 #   if school:
 #       return render(request, 'map.html', {'school': school})
 #   else:
  #      return render('someerror.html')

def show_school(request):
    school = schools_by_key
    if school:
        return render(request, 'map.html', {'school': school})
    else:
        return render('someerror.html')
# Create your views here.
