from django.shortcuts import render,redirect
from myapp.models import Customer,Catagory,Chat
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import Properties
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
# from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request,'index.html')






def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirm_password']
        age=request.POST['age']
        phone=request.POST['phone']
        country=request.POST['country']
        state=request.POST['state']
        district=request.POST['district']
        place=request.POST['place']
        if password==confirmpassword:
            messages.success(request,"registration compleated")
            abc=User.objects.create_user(first_name=fname,last_name=lname,username=username,password=password)
            Customer.objects.create(age=age,phone=phone,country=country,state=state,district=district,place=place,foreign_key_id=abc.id)

            return redirect(log)
        else:
            messages.error(request,"password and confirm password does not match")

    return render(request,'register.html')

def log(request):
    if request.method=='POST':
        username=request.POST['username']
        psw=request.POST['password']
        myuser=authenticate(request,username=username,password=psw)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"login successfully")
            return redirect(mainview) 
        else:
            messages.error(request,"somthing wrong")
            return redirect(log)
    return render(request,'login.html')

def sell(request):
    
    return render(request,'sell.html')


def building(request):
    if request.user.is_authenticated:

        if request.method=='POST':
            img=request.FILES['img']
            country=request.POST['country']
            state=request.POST['state']
            district=request.POST['district']
            name=request.POST['name']        
            phone=request.POST['phone']
            place=request.POST['place']
            price=request.POST['price']
            propert_type=request.POST['property']
            ploat_area=request.POST['area']
            discription=request.POST['disc']
            floar=request.POST['floar']
            current_user=request.user.id
            
            catagoryid=0
            if propert_type=="land":
                catagoryid=1
            elif propert_type=="building":
                catagoryid=2
                
            a=Properties.objects.create(property_image=img,name=name,phone=phone,property_country=country,property_state=state,property_district=district,property_place=place,property_price=price,property_type=propert_type,ploat_area=ploat_area,property_discription=discription,floar=floar,catagoryid_id=2,customerid_id=current_user)
            messages.success(request,"your property added successfully")
            return redirect(profileview)
    else:
        return redirect(log)
    return render(request,'building.html')

def land(request):
    if request.user.is_authenticated:

        if request.method=='POST':
            img=request.FILES['file']
            country=request.POST['country']
            name=request.POST['name']
            phone=request.POST['phone']
            state=request.POST['state']
            district=request.POST['district']
            place=request.POST['place']
            price=request.POST['price']
            propert_type=request.POST['property']
            ploat_area=request.POST['area']
            discription=request.POST['disc']
            current_user=request.user.id
            
            catagoryid=0
            if propert_type=="land":
                catagoryid=1
            elif propert_type=="building":
                catagoryid=2
                
            a=Properties.objects.create(name=name,phone=phone,property_image=img,property_country=country,property_state=state,property_district=district,property_place=place,property_price=price,property_type=propert_type,ploat_area=ploat_area,property_discription=discription,catagoryid_id=1,customerid_id=current_user)
            messages.success(request,"your property added successfully")
            return redirect(profileview)
    else:
        return redirect(log)
    return render(request,'land.html')

def flat(request):
    if request.user.is_authenticated:

        if request.method=='POST':
            img=request.FILES['file']
            country=request.POST['country']
            name=request.POST['name']
            phone=request.POST['phone']
            state=request.POST['state']
            district=request.POST['district']
            place=request.POST['place']
            price=request.POST['price']
            propert_type=request.POST['flat']
            ploat_area=request.POST['area']
            discription=request.POST['disc']
            current_user=request.user.id
            
            catagoryid=0
            if propert_type=="land":
                catagoryid=1
            elif propert_type=="building":
                catagoryid=2
            elif propert_type=="flat":
                catagoryid=3
                
            a=Properties.objects.create(name=name,phone=phone,property_image=img,property_country=country,property_state=state,property_district=district,property_place=place,property_price=price,property_type=propert_type,ploat_area=ploat_area,property_discription=discription,catagoryid_id=3,customerid_id=current_user)
            messages.success(request,"your property added successfully")
            return redirect(profileview)
    else:
        return redirect(log)
    return render(request,'flat.html')

def catagory(request):
    user=request.user
    cati=Catagory.objects.filter(status=0)
    return render(request,'catagories.html',{'catagary':cati})

def mainview(request):
    user=request.user
    allview=Properties.objects.all()
    return render(request,'main.html',{'allview':allview})

def profileview(request):
    if request.user.is_authenticated:
        current_user=request.user.id
        user=User.objects.filter(id=current_user)
        cust=Customer.objects.filter(foreign_key=current_user)
        sellesprop=Properties.objects.filter(customerid=current_user)
        return render(request,'profview.html',{'porfv':user,'data':cust,'prop':sellesprop})
    else:
        return redirect(log)
    return render(request,'profview.html',{'porfv':user,'data':cust,'prop':sellesprop})


def deletesell(request,id):
    dele=Properties.objects.get(id=id)
    dele.delete()
    messages.success(request,'your property succesfully deleted')
    return redirect(profileview)
def edit(request,id):
    a=User.objects.get(id=id)
    b=Customer.objects.get(foreign_key=id)
    
    return render(request,'updateprof.html',{'user':a,'cust':b})

def updatepro(request,id):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        place=request.POST['place']
        phone=request.POST['phone']
        a=User.objects.get(id=id)
        a.first_name=fname
        a.last_name=lname
        print(a)
        a.save()
        b=Customer.objects.get(foreign_key=id)

        b.place=place
        b.phone=phone
        b.save()

        return redirect(profileview)


    return redirect(edit)
    
# def viewland(request):
#     lnd=Properties.objects.filter(property_type='land').values
#     return render(request,'properties.html',{'land':lnd})



# def chat(request,id):
#     if request.method=='POST':
#         name=request.POST['name']
#         com=request.POST['com']
#         Chat.objects.create(name=name,comment=com,key_id=id)
#     return render(request,'chat.html')
# def chatview(request):

#     c=Chat.objects.get(key_id=a.id)
#     return render(request,'chatview.html',{'ch':c})


def property(request,id):    
    if Catagory.objects.filter(id=id,status=0):
        prop=Properties.objects.filter(catagoryid=id)
    else:
        return HttpResponse('not found')
        
    return render(request,'properties.html',{'property':prop})



def search(request):
    query=None
    result=[]
    if request.method=='GET':
        query=request.GET.get('search')
        result=Properties.objects.filter( Q(property_place=query) | Q(property_district=query) | Q(property_type=query) |Q(property_state=query))
        return render(request,'search1.html',{'result':result,'query':query})
    

def viewpropertydetailes(request,id):
    vprop=Properties.objects.filter(id=id)
    return render(request,'viewpropertydetailes.html',{'vprop':vprop})


# def addcart(request,id):
#     user=request.user
#     a=Properties.get(id=id)
#     v=a.add()


def logoutpg(request):
    logout(request)
    return redirect(mainview)
