from django.conf.urls import patterns, include, url
from django.contrib import admin

from api import router

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^game/', include('crafter.urls'), name='crafter'),
    url(r'^admin/', include(admin.site.urls)),
)
