from django.http import HttpResponse
from .models import Entry, Tag

def index(request):
  return HttpResponse("Hello world")

def entry(request, id):
  entry = Entry.objects.get(id=id)
  return HttpResponse('<h1>%s</h1>' % entry.word)