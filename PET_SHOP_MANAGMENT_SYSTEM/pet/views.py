from fileinput import filename
from multiprocessing import context
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from order.models import PetOrder
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from pet.models import Pet
def addpet(request):
    if request.method=="POST":
        ob=Pet()
        ob.pet_name=request.POST.get('pn')
        ob.pet_type=request.POST.get('pt')
        ob.age=request.POST.get('age')
        ob.description=request.POST.get('desc')
        ob.price=request.POST.get('price')
        ob.quantity=request.POST.get('qua')
        myfile=request.FILES["pi"]
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        ob.image=myfile.name
        ob.save()

    return render(request,'pet/pet.html')

def viewpet(request):
    obj1=""
    if request.method=='POST':
        vvv=request.POST.get('pt')
        obj=Pet.objects.filter(pet_type__istartswith=vvv)
        obj1="added to cart"
        context={
            'msg':obj1,
            'ok':obj
            
            
            }
    else:
        ob=Pet.objects.all()
        context={
             
            'ok':ob
    }
    return render(request,'pet/viewpet.html',context)


def addcartt(request,idd):
   
    ss=request.session["regid"]
    
    ob=Pet.objects.get(pet_id=idd)
    obj=PetOrder()
    obj.pet_id=idd
    obj.quantity=1
    obj.reg_id=ss
    obj.price=ob.price
    obj.save()
    # obj1="added to cart"
    # context={
    #     'msg':obj1
    #     }
    return viewpet(request)
    return HttpResponseRedirect("/pet/viewpet/")

