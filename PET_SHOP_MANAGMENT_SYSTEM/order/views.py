from multiprocessing import context
from django.shortcuts import render
from order.models import PetOrder

# Create your views here.
from order.models import PetOrder
def viewpeto(request):
    
    ss=request.session['regid']
    ob=PetOrder.objects.filter(reg_id=ss)
    
    context={
        'ok':ob
    }

    return render(request,'order/viewpetorder.html',context)

def viewpetord(request):
    opp=PetOrder.objects.all()
    context={
        'ope':opp
    }

    return render(request,'order/adminpetorderview.html',context)

def delt(request,idd):
    obj=PetOrder.objects.get(petorder_id=idd).delete()
    return viewpeto(request)
