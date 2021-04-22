from django import forms
from .models import Entry

class EntryForm(forms.Form):
    word = forms.CharField(label="Word", max_length=200)
    definition = forms.CharField(
        label="Definition",
        max_length=1500,
        widget=forms.Textarea
    )

# # should be identical to above
# class EntryForm(forms.Form):
#     model = Entry
#     fields = ['word', 'definition']


    # word = models.CharField(max_length=120)
    # definition = models.TextField(max_length=1500)
    # source = models.TextField(max_length=5000)
    # favorite = models.BooleanField(default=False)
    # private = models.BooleanField(default=False)
    # # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag)
