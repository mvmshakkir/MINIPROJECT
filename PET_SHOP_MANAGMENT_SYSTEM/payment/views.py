from re import A
from django.shortcuts import render
import datetime

# Create your views here.
from payment.models import Payment
from productorder.models import ProductOrder
from order.models import PetOrder

def pay(request):
    ss=request.session['regid']
    ob=ProductOrder.objects.filter(reg_id=ss)
    a=0
    for i in ob:
        amount=i.quantity*i.price
        a=a+amount
        context={
            'x':a
        }
    objl=""
    if request.method=="POST":
        ob=Payment()
        ob.price=request.POST.get('pr')
        ob.card_number=request.POST.get('cn')
        ob.cardholder_name=request.POST.get('chn')
        ob.cvv=request.POST.get('cvv')
        ob.date=datetime.datetime.now()
        ob.save()
        objl= "payment successfull"
    context={
        'msg':objl,
        'x':a
        }      
    return render(request,'payment/payment.html',context)

def viewpay(request):
    ob=Payment.objects.all()
    context={
        'ok':ob
    }
    
    return render(request,'payment/viewpayment.html',context)    

def pet_pay(request):
    ss=request.session['regid']
    
    obc=PetOrder.objects.filter(reg_id=ss)
    b=0
    for i in obc:

        amount1=i.quantity*i.price
        b=b+amount1
        context={
            'y':b
        }

    objl=""
    if request.method=="POST":
        ob=Payment()
        ob.price=request.POST.get('pr')
        ob.card_number=request.POST.get('cn')
        ob.cardholder_name=request.POST.get('chn')
        ob.cvv=request.POST.get('cvv')
        ob.date=datetime.datetime.now()
        
        ob.save()
        objl= "payment successfull"
    context={
        'msg':objl,
        'y':b
        }
       
    
    return render(request,'payment/petpayment.html',context)