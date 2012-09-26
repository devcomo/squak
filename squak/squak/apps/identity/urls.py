"""
Identity Urls
"""
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from squak.apps.identity import views


urlpatterns = patterns('',
    url(r'', include('registration.backends.default.urls')),
    url(r'^$', login_required(views.EditProfile.as_view()),
        name='profile')
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^sign-in/$', 'login', name='login'),
    url(r'^sign-out/$', 'logout', name='logout'),
)
