from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='index'),
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('<int:id>', views.entry, name='entry'),
]
