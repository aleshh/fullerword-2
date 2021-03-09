from django.urls import path

from . import views

urlpatterns = [
  path('', views.list, name='index'),
  path('home/', views.home, name='home'),
  path('add/', views.add, name='add'),
  path('<int:id>', views.entry, name='entry'),
]