from django.urls import path

from . import views

urlpatterns = [
  path('', views.list, name='index'),
  path('home/', views.home, name='home'),
  path('<int:id>', views.entry, name='entry'),
]