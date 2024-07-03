from django.urls import path, re_path
from ProjectApp import views

urlpatterns = [
    re_path(r'^project/$', views.projectAPI),
    re_path(r'^project/([0-9]+)/$', views.projectAPI),
    re_path(r'^repository/$', views.repositoryAPI),
    re_path(r'^repository/([0-9]+)/$', views.repositoryAPI),
    re_path(r'^tracker/$', views.trackerAPI),
    re_path(r'^tracker/([0-9]+)/$', views.trackerAPI),
]
