from django.conf.urls import url

from registration import views

urlpatterns=[
    url('reg/',views.reg)
    
]