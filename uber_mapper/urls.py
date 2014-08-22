from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mapper.views.home', name='home'),
    url(r'^login/', 'mapper.views.login', name='login'),
    url(r'^login_return/', 'mapper.views.login_return', name='login_return'),
    url(r'^trips_feed/', 'mapper.views.trips_feed', name='trips_feed'),

)
