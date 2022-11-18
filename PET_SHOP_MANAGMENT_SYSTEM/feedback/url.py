from django.conf.urls import url

from feedback import views

urlpatterns=[
    url('feed/',views.feedb),
    url('viewfee/',views.viewfeed)
]