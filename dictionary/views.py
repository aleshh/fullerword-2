from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entry, Tag
from .forms import EntryForm


def list(request):
    entries = Entry.objects.all()
    return render(request, 'dictionary/list.html', {"entries": entries})


def add(request):
    if request.method == "POST":
        form = EntryForm(request.POST)

        if form.is_valid():
            entry = Entry()
            entry.word = form.cleaned_data["word"]
            entry.definition = form.cleaned_data["definition"]
            entry.save()

        return HttpResponseRedirect('/%i' % entry.id)
    else:
        form = EntryForm()
    return render(request, 'dictionary/add.html', {"form": form})


def home(request):
    return render(request, 'dictionary/home.html', {})


def edit(request, id):
    if request.POST.get("delete"):
        print(Entry.objects.filter(id=id))
        Entry.objects.filter(id=id).delete()

        return HttpResponseRedirect('/')

    if request.POST.get("edit"):
        print('> Edit')
        entry = Entry.objects.get(id=id)
        # form = EntryForm(entry)

        # return render(request, 'dictionary/add.html', {"form": form})



    print('>>> views:edit redirecting to entry')

    return HttpResponseRedirect('/%s' % id)


def entry(request, id):
    print('> Entry')
    entry = Entry.objects.get(id=id)
    return render(request, 'dictionary/entry.html', {"entry": entry})
