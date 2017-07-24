from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process', views.process, name='process'),
    url(r'^restart', views.clear, name='restart')
]
