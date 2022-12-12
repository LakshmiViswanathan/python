from django.shortcuts import render, HttpResponse,redirect



def index(request):
    # s=Service.objects.all()
    # r = Room.objects.all()
    # return HttpResponse('Hello')
    return render(request, 'index.html')