from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#dajaxice_autodiscover()

urlpatterns = patterns('',
     url(r'^', include('music.urls')),
     url(r'^', include('PRICD.urls')),
     #url(r'^app/', include('apps.heatmap.urls'), name='app'),
     #url(r'^sends/', include('apps.heatmap.urls')),
     #url(r'^input/', include('apps.heatmap.urls'), name='input'),
     #url(dajaxice_config.dajaxice_url, include('dajaxice')),
     
     # Examples:
     # url(r'^$', 'generic_django_project.views.home', name='home'),
     # url(r'^generic_django_project/', include('generic_django_project.foo.urls')),

     # Uncomment the admin/doc line below to enable admin documentation:
     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     # Uncomment the next line to enable the admin:
     # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()






















