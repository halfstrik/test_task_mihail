from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^goods/', include('goods.urls', namespace='goods')),
                       url(r'^admin/', include(admin.site.urls)), )
