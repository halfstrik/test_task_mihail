from django.conf.urls import patterns, url
from goods import views

urlpatterns = patterns('',
                       url(r'^stuff$', views.get_stuff_view, name=u'stuff'),
                       url(r'^properties$', views.get_property_values_view, name=u'properties'))
