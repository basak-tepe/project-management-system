from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ProjectApp.models import Projects, Repository, Tracker
from ProjectApp.serializers import ProjectsSerializer, RepositorySerializer, TrackerSerializer
from django.shortcuts import get_object_or_404

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
        try:
            project = get_object_or_404(Projects, pk=id)
            project_data = JSONParser().parse(request)
            projects_serializer = ProjectsSerializer(project, data=project_data)
            if projects_serializer.is_valid():
                projects_serializer.save()
                return JsonResponse({'message': 'Updated Successfully'}, status=200)
            return JsonResponse(projects_serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    elif request.method == 'DELETE':
        project = get_object_or_404(Projects, pk=id)
        project.delete()
        return JsonResponse('Deleted Successfully', safe=False)

@csrf_exempt
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
        return JsonResponse(repositories_serializer.errors, status=400)

    
    elif request.method == 'PUT':
        try:
            repository = get_object_or_404(Repository, pk=id)
            repository_data = JSONParser().parse(request)
            repositories_serializer = RepositorySerializer(repository, data=repository_data)
            if repositories_serializer.is_valid():
                repositories_serializer.save()
                return JsonResponse({'message': 'Updated Successfully'}, status=200)
            return JsonResponse(repositories_serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == 'DELETE':
        repository = get_object_or_404(Repository, pk=id)
        repository.delete()
        return JsonResponse('Deleted Successfully', safe=False)

@csrf_exempt
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
        return JsonResponse(trackers_serializer.errors, status=400)
    
    elif request.method == 'PUT':
        try:
            tracker = get_object_or_404(Tracker, pk=id)
            tracker_data = JSONParser().parse(request)
            trackers_serializer = TrackerSerializer(tracker, data=tracker_data)
            if trackers_serializer.is_valid():
                trackers_serializer.save()
                return JsonResponse({'message': 'Updated Successfully'}, status=200)
            return JsonResponse(trackers_serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == 'DELETE':
        tracker = get_object_or_404(Tracker, pk=id)
        tracker.delete()
        return JsonResponse('Deleted Successfully', safe=False)

