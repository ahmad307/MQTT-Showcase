from django.conf.urls import url
from mqtt import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]