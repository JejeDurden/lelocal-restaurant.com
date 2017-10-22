from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^carte/$', views.carte, name='carte'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^edito/$', views.edito, name='edito'),
    ]
