from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    # password
    use_source = models.BooleanField(default=True)
    use_favorites = models.BooleanField(default=True)

class Tag(models.Model):
    name = models.CharField(max_length=60)

class Entry(models.Model):
    word = models.CharField(max_length=120)
    definition = models.TextField(max_length=1500)
    source = models.TextField(max_length=5000)
    favorite = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
