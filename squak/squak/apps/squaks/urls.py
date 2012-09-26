"""
Identity Urls
"""
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from squak.apps.squaks import views


urlpatterns = patterns('',
    url(r'^list/$', views.SquakList.as_view(), name='global-squak-list'),
    url(r'^create/$', login_required(views.CreateSquak.as_view()),
        name='create-squak'),

    url(r'^(?P<username>[a-zA-Z0-9_.-]+)/', views.SquakList.as_view(),
        name='user-squak-list'),
)
