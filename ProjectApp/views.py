from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ProjectApp.models import Projects, Repository, Tracker
from ProjectApp.serializers import ProjectsSerializer, RepositorySerializer, TrackerSerializer
from django.shortcuts import get_object_or_404

class projectAPI(APIView):
    def get(self, request, id=None):
        if id:
            project = get_object_or_404(Projects, pk=id)
            serializer = ProjectsSerializer(project)
            return Response(serializer.data)
        else:
            projects = Projects.objects.all()
            serializer = ProjectsSerializer(projects, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Added Successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        project = get_object_or_404(Projects, pk=id)
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated Successfully', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        project = get_object_or_404(Projects, pk=id)
        project.delete()
        return Response('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)

class repositoryAPI(APIView):
    def get(self, request, id=None):
        if id:
            repository = get_object_or_404(Repository, pk=id)
            serializer = RepositorySerializer(repository)
            return Response(serializer.data)
        else:
            repositories = Repository.objects.all()
            serializer = RepositorySerializer(repositories, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = RepositorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Added Successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        repository = get_object_or_404(Repository, pk=id)
        serializer = RepositorySerializer(repository, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated Successfully', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        repository = get_object_or_404(Repository, pk=id)
        repository.delete()
        return Response('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)

class trackerAPI(APIView):
    def get(self, request, id=None):
        if id:
            tracker = get_object_or_404(Tracker, pk=id)
            serializer = TrackerSerializer(tracker)
            return Response(serializer.data)
        else:
            trackers = Tracker.objects.all()
            serializer = TrackerSerializer(trackers, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = TrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Added Successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        tracker = get_object_or_404(Tracker, pk=id)
        serializer = TrackerSerializer(tracker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated Successfully', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        tracker = get_object_or_404(Tracker, pk=id)
        tracker.delete()
        return Response('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
