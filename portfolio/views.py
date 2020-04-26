from django.shortcuts import render

def index(request):
    return render(request,'portfolio/index.html',{})

def project_cards(request):
    return render(request,'portfolio/projects-grid-cards.html',{})

def cv(request):
    return render(request, 'portfolio/cv.html', {})

def hire_me(request):
    return render(request, 'portfolio/hire-me.html', {})