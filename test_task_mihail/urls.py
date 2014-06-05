from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^goods/', include(u'goods.urls', namespace=u'goods')),
                       url(r'^admin/', include(admin.site.urls)), )
