from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, logout
from service.models import Service
from contact.models import Contact
from land.models import Room



def index(request):
    # return HttpResponse('Hello')
    s=Service.objects.all()
    return render(request, 'index.html', {'s':s})

def service(request):
    # return HttpResponse('Hello')
    s=Service.objects.all()
    return render(request, 'service.html', {'s':s})

def show_service(request):
    # return HttpResponse('Hello')
    if request.method=='POST':
        pk=request.POST.get('pk')
        s=Service.objects.get(pk=pk)
        return render(request, 'show_service.html', {'s':s}) 

def contact(request):
    # return HttpResponse('Hello')
    return render(request, 'contact.html')

def handle_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        msg=request.POST.get('msg')
        c= Contact(name=name, email=email, subject=subject, message=msg)
        c.save()
        return redirect('contact')

def mylogout(request):
    logout(request)
    return redirect('home')
def detail(request):
    if request.method=="POST":
        pk=request.POST.get('pk')
        r=Room.objects.get(pk=pk)     
      
    # return HttpResponse('Hello')
        return render(request, 'detail.html', {'r':r})    