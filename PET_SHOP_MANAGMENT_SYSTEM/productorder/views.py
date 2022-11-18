from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render

# Create your views here.
from productorder.models import ProductOrder
# def viewproord(request):
#     ob=ProductOrder.objects.all()
#     context={
#         'ok':ob
#     }
#     return render(request,'productorder/vieproductorder.html',context)
    
def proord(request):
    ss=request.session['regid']
    obb=ProductOrder.objects.filter(reg_id=ss)
    context={
        'okk':obb
    }
    return render(request,'productorder/vieproductorder.html',context)
def viewad(request):
    obbb=ProductOrder.objects.all()
    context={
        'op':obbb
        
    }
    return render(request,'productorder/adminorderview.html',context)
def delpr(request,idd):
    obj=ProductOrder.objects.get(productorder_id=idd).delete()
    return proord(request)