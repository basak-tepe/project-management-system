from django.db import models

# Create your models here.
'''
    An interface to add new projects with details such as name, slug, description, and
language.

○ User should be able to add repositories and trackers to the project while creating
new projects. A repository should also have the following fields: title, URL, type,
email, and token. A tracker should also have the following fields: title, URL, type,
email, and token.
○ type field for the repository should have the following options: GitHub, GitLab,
and Bitbucket.
○ type field for the tracker should have the following options: GitHub, GitLab, and
Jira.
○ A data table to list all project items, displaying their details clearly.
○ Options to edit and delete projects directly from the data table, ensuring ease of
management.
'''

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
    TrackerID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    URL = models.URLField()
    type = models.CharField(max_length=100)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.title