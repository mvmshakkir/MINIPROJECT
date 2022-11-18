from django.shortcuts import render
from login.models import Login
# Create your views here.
from registration.models import Registration
def reg(request):
    if request.method=="POST":
        ob=Registration()
        ob.first_name=request.POST.get('fn')
        ob.last_name=request.POST.get('ln')
        ob.user_name=request.POST.get('sn')
        ob.password=request.POST.get('pw')
        ob.conform_password=request.POST.get('pw')
        ob.gender=request.POST.get('gen')
        ob.email=request.POST.get('email')
        ob.place=request.POST.get('place')
        ob.post=request.POST.get('post')
        ob.pin=request.POST.get('pin')
        ob.phone=request.POST.get('phone')
        ob.save()
        obb=Login()
        obb.user_name=ob.user_name
        obb.password=ob.password
        obb.type="user"
        obb.reg_id=ob.reg_id
        obb.save()
    return render(request,'registration/registration.html')
    


