from django.conf.urls import url
from . import views
                    
# urlpatterns = [
#     url(r'^$', views.index),
# ]

urlpatterns = [
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<my_val>\d+)$', views.show),
    url(r'^(?P<my_val>\d+)/edit$', views.edit),
    url(r'^(?P<id>[0-9]+)/delete$', views.delete),
    url(r'^bears/(?P<my_val>\d+)$', views.another_method),
    url(r'^bears/(?P<name>\w+)/poke$', views.yet_another),
    url(r'^(?P<id>[0-9]+)/(?P<color>\w+)$', views.one_more),
]