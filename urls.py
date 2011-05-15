from django.conf.urls.defaults import patterns, include, url

from tag import views 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<tag>[^/]+)/$', views.redirect),
    url(r'^(?P<tag>[^/]+)/edit/$', views.edit),
)
