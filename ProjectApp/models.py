from django.db import models

class Projects(models.Model):
    projectID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    language = models.CharField(max_length=50)
    repositories = models.ManyToManyField('Repository', related_name='projects', blank=True)
    trackers = models.ManyToManyField('Tracker', related_name='projects', blank=True)

    def __str__(self):
        return self.name

class Repository(models.Model):
    repositoryID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    URL = models.URLField()
    type = models.CharField(max_length=50)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tracker(models.Model):
    trackerID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    URL = models.URLField()
    type = models.CharField(max_length=50)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title
