from django.conf.urls import url,include
from django.contrib import admin
from mqtt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',include('mqtt.urls')),
    url(r'^ajaxconnect', views.post),
    url(r'^ajaxdisconnect',views.post_disconnect),
]
