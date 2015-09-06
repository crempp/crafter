from django.conf.urls import patterns, url

from crafter import views

urlpatterns = patterns('',

    url(r'^(?P<game_id>\d+)/$', views.GameView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
)