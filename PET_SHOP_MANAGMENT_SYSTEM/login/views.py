from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from login.models import Login
def log(request):
    if request.method=='POST':
        name=request.POST.get('sn')
        password=request.POST.get('password')
        obj =Login.objects.filter(user_name=name,password=password)
        tp=""
        for ob in obj:
            tp=ob.type
            regid=ob.reg_id
            if tp == "admin":
                request.session["regid"]=regid
                return HttpResponseRedirect('/temp/index/')
            elif tp =="user":
                request.session['regid']=regid
                return HttpResponseRedirect('/temp/user/')
        else:
            objl= "username or password incorrect...... please try again.....!"
            context={
                'msg':objl,
            }
            return render(request,'login/login.html',context)    




    return render(request,'login/login.html')
