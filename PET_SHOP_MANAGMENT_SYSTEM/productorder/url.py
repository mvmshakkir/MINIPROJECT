from django.conf.urls import url

from productorder import views

urlpatterns=[
    # url('proord/',views.viewproord)
    url('prodr/',views.proord),
    url('dp/(?P<idd>\w+)',views.delpr),
    url('viewadmin/',views.viewad)
   
   
]