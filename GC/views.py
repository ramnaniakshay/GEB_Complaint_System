from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages,sessions
from GC.forms import UserDForm  
from GC.models import UserD,Admin
from os import stat
from datetime import date
from django.http import HttpResponse
import mysql.connector as mcdb

conn = mcdb.connect(host="localhost", user="root", password="", database='gc')
print('Successfully connected to database')
cur = conn.cursor()
today = date.today()

def login(request):
    if request.method=='POST':
        try:
                userd = UserD.objects.get(email=request.POST['email'],password=request.POST['password'])
                request.session['email']=request.POST['email']
                return render(request,'dashboardc.html')
        except Exception as e1:
            try:
                admin = Admin.objects.get(email=request.POST['email'],password=request.POST['password']) 
                request.session['email']=request.POST['email']       
                return render(request,'home.html')
            except:
                messages.info(request,'invalid username or password')
                return render(request,'login.html')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        userd = UserD()
        userd.name = request.POST['name']
        userd.gender = request.POST['gender']
        userd.birthdate = request.POST['birthdate']
        userd.aadharno = request.POST['aadharno']
        userd.address = request.POST['address']
        userd.email = request.POST['email']
        userd.password = request.POST['password']
        userd.status="ACTIVE"
        userd.role="USER"

        if UserD.objects.filter(email=userd.email).exists():
            messages.info(request,'Email taken')
            return redirect('register')
        else:
            userd.save()
            return redirect('login')
    else:    
        return render(request,'register.html'   )

def home(request):
    cur.execute("SELECT (SELECT COUNT(uid) FROM gc_userd) AS usercount,(SELECT COUNT(complaintid) FROM complaints) AS complaintcount,(SELECT COUNT(complaintid) FROM complaints where status='PENDING') AS pendingcount")
    data=cur.fetchall()
    print(data)
    return  render(request,'home.html',{'countnumber':data})

def pendingcomplaintslisting(request):
    cur.execute("SELECT gc_userd.name, gc_userd.address, complaints.description, complaints.rdate, employee.empname, complaints.fdate, complaints.status,complaints.complaintid from complaints inner join gc_userd on gc_userd.email=complaints.email left join employee on employee.empid=complaints.empid where complaints.status!='FINISHED'")
    data=cur.fetchall()
    return render(request,'viewpending.html',{'complaints':data})

def complaintslisting(request):
    cur.execute("SELECT gc_userd.name, gc_userd.address, complaints.description, complaints.rdate, employee.empname, complaints.fdate, complaints.status, complaints.complaintid from complaints inner join gc_userd on gc_userd.email=complaints.email left join employee on employee.empid=complaints.empid")
    data=cur.fetchall()
    return render(request,'view.html',{'complaints':data})

def viewuser(request):
    cur.execute("SELECT * FROM gc_userd")
    data = cur.fetchall()
    print(list(data))
    return render(request, 'viewusers.html', {'user': data})   


def addcc(request):
    return render(request, 'addcc.html')


def addcomplaint(request):
    return render(request, 'addcomplaint.html')

def viewcomplaint(request):
    email=request.session['email']
    cur.execute("SELECT * FROM complaints where email='{}'".format(email))
    data = cur.fetchall()
    return render(request, 'viewcc.html', {'user': data})

def complaintinserted(request):
    if request.method == 'POST':
        email=request.session['email']
        status="RECIEVED"
        rdate = today.strftime("%d-%m-%Y")
        description = request.POST['description']
        cur.execute("INSERT INTO `complaints`(`rdate`,`description`,`status`,`email`) VALUES ('{}','{}','{}','{}')".format(rdate,description,status,email))
        conn.commit()
        return render(request,'dashboardc.html')
    else:
        return render(request,'addcc.html') 


def updateform(request,id):
    cur.execute("SELECT gc_userd.name, gc_userd.address, complaints.description, complaints.rdate, employee.empname, complaints.fdate, complaints.status, complaints.complaintid from complaints inner join gc_userd on gc_userd.email=complaints.email left join employee on employee.empid=complaints.empid where complaintid={}".format(id))
    data=cur.fetchone()
    cur.execute("SELECT * from employee")
    empdata=cur.fetchall()
    print(empdata)
    return render(request,'editpending.html',{'complaints':data,'employee':empdata})


def complaintupdate(request):
    if request.method=="POST":
        id=request.POST['id']
        status=request.POST['status']
        empid=request.POST['employee']
        fdate=request.POST['fdate']
        cur.execute("update complaints set status='{}', empid='{}', fdate='{}' where complaintid='{}'".format(status,empid,fdate,id))
        conn.commit()
        return redirect(complaintslisting)
    else:
        return redirect(complaintslisting)


""" def addcc(request):
    try:
        if request.session['email'] is not None:
            return render(request,'addcc.html')
    except Exception as e:
        return render(request,'login.html') """

def logout(request):
    auth.logout(request)
    return render(request,'login.html')