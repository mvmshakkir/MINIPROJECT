from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request,'temp/main.html')

def index(request):
    return render(request,'temp/index.html')    

def user(request):
    return render(request,'temp/user.html')    