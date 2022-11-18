from django.conf.urls import url
from django.urls import URLPattern

from temp import views

urlpatterns=[
    url('main/',views.main),
    url('user/',views.user),
    url('index/',views.index),
    ]
