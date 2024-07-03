from rest_framework import serializers
from ProjectApp.models import Projects, Repository, Tracker

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ('repositoryID', 'title', 'URL', 'type', 'email', 'token')

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ('trackerID', 'title', 'URL', 'type', 'email', 'token')

class ProjectsSerializer(serializers.ModelSerializer):
    repositories = RepositorySerializer(many=True, read_only=True)
    trackers = TrackerSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ('projectID', 'name', 'slug', 'description', 'language', 'repositories', 'trackers')
