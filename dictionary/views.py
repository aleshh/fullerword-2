from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry, Tag
from .forms import CreateNewEntry

def list(request):
    entries = Entry.objects.all()
    return render(request, 'dictionary/list.html', {"entries": entries})

def add(request):
    form = CreateNewEntry()
    return render(request, 'dictionary/add.html', {"form": form})

def home(request):
    return render(request, 'dictionary/home.html', {})

def entry(request, id):
    entry = Entry.objects.get(id=id)
    return render(request, 'dictionary/entry.html', { "word": entry.word })

    # return HttpResponse('<h1>%s</h1>' % entry.word)