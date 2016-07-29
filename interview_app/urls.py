from django.conf.urls import patterns, url
from interview_app import views

urlpatterns = patterns('',

                       url(r'^(?P<url_parameter>.+)/$',
                           views.index, name='index'),
                       )
