from django.shortcuts import render,HttpResponse
from Home.models import Contact

def home(request):
    #return HttpResponse("This is working")
    return render(request,'index.html')
def Education(request):
    return render(request,'Education.html')
def Projects(request):
    return render(request,'Projects.html')
def contact(request):
    if request.method=="POST":
        print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        Phone=request.POST['phone']
        desc=request.POST['message']
        ins = Contact(name=name,email=email,phone=Phone,desc=desc)
        ins.save()
        print('the data is saved')
    return render(request,'contact.html')


# Create your views here.
