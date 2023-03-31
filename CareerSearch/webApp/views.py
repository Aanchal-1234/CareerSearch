from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def occupations(request):
    return render(request, 'occupations.html')

def softwareEngineer(request):
    return render(request, 'softwareEngineer.html')

def doctor(request):
    return render(request, 'doctor.html')

def actuary(request):
    return render(request, 'actuary.html')

def mediaAnalyst(request):
    return render(request, 'mediaAnalyst.html')