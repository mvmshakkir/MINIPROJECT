from django.conf.urls import url

from pet import views

urlpatterns=[
    url('adpet/',views.addpet),
    url('viewpt/',views.viewpet),
     url('addcartt/(?P<idd>\w+)',views.addcartt),
]