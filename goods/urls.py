from django.conf.urls import patterns, url
from goods import views

urlpatterns = patterns('',
                       url(r'^$', views.StuffIndexView.as_view(), name='stuff_index'), )
