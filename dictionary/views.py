from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entry, Tag
from .forms import CreateNewEntry


def list(request):
    entries = Entry.objects.all()
    return render(request, 'dictionary/list.html', {"entries": entries})


def add(request):
    if request.method == "POST":
        form = CreateNewEntry(request.POST)

        if form.is_valid():
            entry = Entry()
            entry.word = form.cleaned_data["word"]
            entry.definition = form.cleaned_data["definition"]
            entry.save()

        return HttpResponseRedirect('/%i' % entry.id)
    else:
        form = CreateNewEntry()
    return render(request, 'dictionary/add.html', {"form": form})


def home(request):
    return render(request, 'dictionary/home.html', {})


def entry(request, id):
    if request.POST.get("delete"):
        Entry.objects.filter(id=id).delete()
        return HttpResponseRedirect('/')

    entry = Entry.objects.get(id=id)
    return render(request, 'dictionary/entry.html', {"entry": entry})
