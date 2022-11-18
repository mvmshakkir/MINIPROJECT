from itertools import product
import ssl
from unicodedata import name
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from order.models import PetOrder
from productorder.models import ProductOrder

# Create your views here.
from product.models import Product
def addpro(request):
    if request.method=="POST":
        ob=Product()
        ob.product_name=request.POST.get('pdn')
        ob.price=request.POST.get('pr')
        ob.description=request.POST.get('desc')
        ob.quantity=request.POST.get('stc')
        myfile=request.FILES["img"]
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        ob.image=myfile.name

        ob.save()
    return render(request,'product/product.html')

def viepro(request):
    ss=request.session["regid"]
    if request.method=='POST':
        if  request.POST.get('pdn'):
            vv=request.POST.get('pdn')
            obj=Product.objects.filter(product_name__istartswith=vv)
            context={
                'ok':obj
            }
        else:
            ob=Product.objects.all()
            context={
                'ok':ob
            }
            for o in ob:
                vv=request.POST.get('no'+str(o.product_id))
                if vv!='':
                    if int(vv)>0:
                        print(vv)
                        prdid=o.product_id
                        qty=vv
                        obj=ProductOrder()
                        obj.product_id=o.product_id
                        obj.quantity=vv
                        obj.reg_id=ss
                        obj.price=o.price
                        obj.save()
    else:
        ob=Product.objects.all()
        context={
            'ok':ob
        }
    return render(request,'product/view_product.html',context)    

def addcart(request,idd):
    ss=request.session["regid"]
    ob=Product.objects.get(product_id=idd)
    
    # # if request.method=="POST":
    obj=ProductOrder()
    obj.product_id=idd
    obj.quantity=1
    obj.reg_id=ss
    obj.price=ob.price

    obj.save()
    
    return HttpResponseRedirect("/prduct/viewproduct/")    
