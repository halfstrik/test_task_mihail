from django.conf.urls import patterns, include, url

from django.contrib import admin
from goods.views import home_view
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', home_view, name=u'home'),
                       url(r'^goods/', include(u'goods.urls', namespace=u'goods')),
                       url(r'^admin/', include(admin.site.urls)), )
