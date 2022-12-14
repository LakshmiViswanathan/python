from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, logout
from service.models import Service
from contact.models import Contact
from land.models import Room
from booking.models import Book


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

def handle_add_booking(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # b = Book.objects.filter(user_id=request.user.pk)
            rpk=request.POST.get('rpk')
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            number=request.POST.get('number')
            country=request.POST.get('country')
            pob=request.POST.get('pob')
            noa=request.POST.get('noa')
            noc=request.POST.get('noc')
            sr=request.POST.get('sr')
            if len(number)>10:
                e='Enter Correct Mobile Number'
                return render(request, 'seller/404.html', {'e':e})
            u=Room.objects.get(pk=rpk)
            print(u.user_id)
            b=Book(booking_username=request.user.username, user_id=u.user_id, room_id=rpk, fname=fname, lname=lname, email=email, number=number, country=country, pob=pob, noa=noa, noc=noc, sr=sr)
            b.save()
            e='Order has been placed'
            return render(request, 'seller/404.html', {'e':e})     
        else:
            return redirect('home')
    else: 
        e='Please Login Before Ordering'
        return render(request, 'seller/404.html', {'e':e})


def delete_booking(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pk=request.POST.get('pk')
            b = Book.objects.get(pk=pk)
            b.delete()
            return redirect('seller_panel')    
    else:
        return redirect('home')

def delete_booking_user(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pk=request.POST.get('pk')
            b = Book.objects.get(pk=pk)
            b.delete()
            return redirect('user_panel')    
    else:
        return redirect('home')

def edit_booking_user(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pk=request.POST.get('pk')
            b = Book.objects.get(pk=pk)
            return render(request, "user/edit_booking.html", {'b':b})    
    else:
        return redirect('home')

def handle_edit_booking(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            bpk=request.POST.get('pk')
            fname=request.POST.get('f_name')
            lname=request.POST.get('l_name')
            email=request.POST.get('email')
            number=request.POST.get('mobile')
            country=request.POST.get('country')
            pob=request.POST.get('pob')
            noa=request.POST.get('noa')
            noc=request.POST.get('noc')
            sr=request.POST.get('sr')
            # u=Book.objects.get(pk=bpk)
            # print(u.user_id)
            if len(number)>10:
                e='Enter Correct Mobile Number'
                return render(request, 'seller/404.html', {'e':e})
            
            r=Book.objects.get(pk=bpk)
            r.fname=fname
            r.lname=lname
            r.email=email
            r.number=number
            r.country=country
            r.pob=pob
            r.noa=noa
            r.noc=noc
            r.sr=sr
            r.save()
            
            # myuser= authenticate(username=u_name, password=password)
            # if myuser is not None:
            #     mylogin(request, myuser)
            #     # return render(request, 'seller/index.html')
            #     return redirect('seller_panel')
            # else:
            return redirect('user_panel')
        
        else:
            return redirect('contact')
        # a=Activation.objects.get(user_id=request.user.pk)
        # return render(request, "seller/post_ad.html")    
    else:
        return redirect('home')




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