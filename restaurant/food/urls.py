from django.conf.urls import url
from restaurant.food import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'api/list', views.get_rest_list, name='get_rest_list'),
]
