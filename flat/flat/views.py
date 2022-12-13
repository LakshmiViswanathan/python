from django.shortcuts import render, HttpResponse,redirect
from service.models import Service


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