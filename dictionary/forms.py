from django import forms

class CreateNewEntry(forms.Form):
    word = forms.CharField(label="Word", max_length=200)
    definition = forms.CharField(label="Definition", max_length=1500, widget=forms.Textarea)



    # word = models.CharField(max_length=120)
    # definition = models.TextField(max_length=1500)
    # source = models.TextField(max_length=5000)
    # favorite = models.BooleanField(default=False)
    # private = models.BooleanField(default=False)
    # # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag)
