from django.urls import path
from ProjectApp.views import projectAPI, repositoryAPI, trackerAPI

urlpatterns = [
    path('project/', projectAPI.as_view(), name='project_list_create'),
    path('project/<int:id>/', projectAPI.as_view(), name='project_detail_update_delete'),
    path('repository/', repositoryAPI.as_view(), name='repository_list_create'),
    path('repository/<int:id>/', repositoryAPI.as_view(), name='repository_detail_update_delete'),
    path('tracker/', trackerAPI.as_view(), name='tracker_list_create'),
    path('tracker/<int:id>/', trackerAPI.as_view(), name='tracker_detail_update_delete'),
]
