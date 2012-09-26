from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from squak.apps.squaks.views import HomePage

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomePage.as_view(), name='homepage'),
    url(r'^identity/', include('squak.apps.identity.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^', include('squak.apps.squaks.urls')),
)
