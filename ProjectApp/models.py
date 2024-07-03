from django.db import models

class Projects(models.Model):
    projectID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=100)
    repositories = models.ManyToManyField('Repository', blank=True)
    trackers = models.ManyToManyField('Tracker', blank=True)

    def __str__(self):
        return self.name

class Repository(models.Model):
    repositoryID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    URL = models.URLField()
    type = models.CharField(max_length=100)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Tracker(models.Model):
    trackerID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    URL = models.URLField()
    type = models.CharField(max_length=100)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title