from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.book),
    url(r'^add_book$', views.add_book),
    url(r'^authors$', views.author),
    url(r'^add_author$', views.add_author),
    url(r'^books/(?P<id>[0-9]+)$', views.view_book)
]