__author__ = 'neil'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<journey_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.listJourneys(), name='listJourneys'),
    url(r'^your-name', views.get_name, name='name'),
]