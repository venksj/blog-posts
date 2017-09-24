from django.conf.urls import url
from .views import post_list
#from . import views

urlpatterns = [ 
        #url(r'^$', views.post_list, name='post_list'),
        url(r'^$', post_list, name='post_list'),
]
