from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('/projects-cards',views.project_cards, name="project-cards"),
    path('/cv',views.cv,name="cv"),
    path('/hire-me',views.hire_me,name="hire_me"),
]
