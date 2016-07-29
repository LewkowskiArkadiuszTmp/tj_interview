from django.conf.urls import patterns, include, url
from django.contrib import admin
#from interview_app import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^interview_app/', include('interview_app.urls')),
                       )
