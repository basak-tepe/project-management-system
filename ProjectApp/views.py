from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ProjectApp.models import Projects, Repository, Tracker
from ProjectApp.serializers import ProjectsSerializer, RepositorySerializer, TrackerSerializer

@csrf_exempt

def projectAPI(request, id=0):
    if request.method == 'GET':
        projects = Projects.objects.all()
        projects_serializer = ProjectsSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        projects_serializer = ProjectsSerializer(data=project_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        project_data = JSONParser().parse(request)
        project = Projects.objects.get(projectID=project_data['projectID'])
        projects_serializer = ProjectsSerializer(project, data=project_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        project = Projects.objects.get(projectID=id)
        project.delete()
        return JsonResponse('Deleted Successfully', safe=False)
    
def repositoryAPI(request, id=0):
    if request.method == 'GET':
        repositories = Repository.objects.all()
        repositories_serializer = RepositorySerializer(repositories, many=True)
        return JsonResponse(repositories_serializer.data, safe=False)
    elif request.method == 'POST':
        repository_data = JSONParser().parse(request)
        repositories_serializer = RepositorySerializer(data=repository_data)
        if repositories_serializer.is_valid():
            repositories_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        repository_data = JSONParser().parse(request)
        repository = Repository.objects.get(repositoryID=repository_data['repositoryID'])
        repositories_serializer = RepositorySerializer(repository, data=repository_data)
        if repositories_serializer.is_valid():
            repositories_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        repository = Repository.objects.get(repositoryID=id)
        repository.delete()
        return JsonResponse('Deleted Successfully', safe=False)
    
def trackerAPI(request, id=0):
    if request.method == 'GET':
        trackers = Tracker.objects.all()
        trackers_serializer = TrackerSerializer(trackers, many=True)
        return JsonResponse(trackers_serializer.data, safe=False)
    elif request.method == 'POST':
        tracker_data = JSONParser().parse(request)
        trackers_serializer = TrackerSerializer(data=tracker_data)
        if trackers_serializer.is_valid():
            trackers_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        tracker_data = JSONParser().parse(request)
        tracker = Tracker.objects.get(trackerID=tracker_data['trackerID'])
        trackers_serializer = TrackerSerializer(tracker, data=tracker_data)
        if trackers_serializer.is_valid():
            trackers_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        tracker = Tracker.objects.get(trackerID=id)
        tracker.delete()
        return JsonResponse('Deleted Successfully', safe=False)