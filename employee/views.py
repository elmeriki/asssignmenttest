from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from employee.models import Employee
from django.contrib import messages
from django.contrib.auth.models import User,auth


def welcome(request):
    return render(request,'login.html')


def dashboard(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passcode = request.POST['passcode']
        user = auth.authenticate(username=uname,password=passcode)
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            messages.info(request,"invalid login details")
            return redirect("/")
    else:
        return render(request,"login.html")  
    
    

def insert(request):
    if request.method == "POST":
        emp = Employee()
        emp.fnames = request.POST['fname']
        emp.email = request.POST['email']
        emp.phone = request.POST['phone']
        emp.addres = request.POST['address']
        emp.save()
        messages.info(request,'Employee has been registered successfully')
        return render(request,'index.html')
    else:
        return redirect(request,'insert')
        

def deleteform(request):
    return render(request,'delete.html')

def deletequery(request):
    if request.method == "POST" and request.method !="GET":
        email = request.POST['email']
        Employee.objects.filter(email=email).delete()
        messages.info(request,'Employee has been deleted Ok')
        return render(request,'index.html')
    else:
        return redirect(request,'deleteform')
    
def logout(request):
    auth.logout(request)
    return redirect("/")