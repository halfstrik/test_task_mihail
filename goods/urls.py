from django.conf.urls import patterns, url
from goods import views

urlpatterns = patterns('',
                       url(r'^stuff$', views.get_stuff_view, name=u'stuff'), )
