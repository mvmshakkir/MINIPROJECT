from django.conf.urls import url

from order import views

urlpatterns=[
    url('ord/',views.viewpeto),
    url('dt/(?P<idd>\w+)',views.delt),
     url('viewpetorder/',views.viewpetord)
   
]