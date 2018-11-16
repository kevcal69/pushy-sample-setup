'''View '''
from django.conf.urls import url

from contrib import views


urlpatterns = [
    url(r'^service-worker.js$', views.ServiceWorker.as_view(), name='service-worker'),
    url(r'^presence$', views.PresenceTestView.as_view(), name='presence'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
