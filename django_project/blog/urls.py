#dodajemy plik URLS do którego prowadzi główny urls z django_project

from django.urls import path
from . import views # . oznacza z bierzącego katalogu importujemy views w której mamy fukncje home

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name='blog-about'),

]