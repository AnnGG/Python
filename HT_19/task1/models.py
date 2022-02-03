from django.db import models

class Askstor(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.IntegerField()
    id_ask = models.IntegerField(primary_key=True)
    score = models.IntegerField()
    text = models.TextField()
    time = models.IntegerField()
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id_ask)

class Showstor(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField()
    text = models.TextField()
    time = models.IntegerField()
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Newstor(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    score = models.CharField(max_length=200)
    time = models.IntegerField(default=None)
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default=None)
    text = models.TextField()

    def __str__(self):
        return self.title

class Jobstor(models.Model):
    by = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    score = models.CharField(max_length=200)
    text = models.TextField()
    time = models.IntegerField()
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.title


