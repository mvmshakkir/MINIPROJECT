from django.shortcuts import render
import datetime
# Create your views here.
from feedback.models import Feedback
def feedb(request):
    ss=request.session['regid']
    if request.method=="POST":
        fb=Feedback()
        fb.rating=request.POST.get('rat')
        fb.feedback=request.POST.get('fb')
        fb.date=datetime.datetime.now()
        fb.reg_id=ss
        fb.save()
    return render(request,'feedback/feedback.html')

def viewfeed(request):
    ob=Feedback.objects.all()
    context={
        'ok':ob
    }
    return render(request,'feedback/viewfeedback.html',context)