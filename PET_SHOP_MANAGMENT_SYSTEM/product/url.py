from django.conf.urls import url

from product import views

urlpatterns=[
    url('pro/',views.addpro),
    url('viewproduct/',views.viepro),
    url('addcart/(?P<idd>\w+)',views.addcart),
]