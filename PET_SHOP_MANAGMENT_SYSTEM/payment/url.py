from django.conf.urls import url

from payment import views

urlpatterns=[
    url('pay/',views.pay),
    url('viewp/',views.viewpay),
    url('aab/',views.pet_pay),
]