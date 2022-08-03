from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import TeacherInfo, StudentInfo

# Create your views here.

def index(request):
    return render(request, 'index.html')
def login_user(request):
    # u = User.objects.get(username = 'John Teacher')
    # u.set_password('12345')
    # u.save()
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Login invalid please check username or passowrd')
            return render(request,'login.html')
    else:
        messages.add_message(request, messages.ERROR, '')
        return render(request,'login.html')
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def teach_reg(request):
    if request.method == 'POST':
        try:
            u = User()
            u.username = request.POST['uname']
            u.email = request.POST['email']
            u.password = request.POST['pwd']
            u.save()
            u = User.objects.get(username = request.POST['uname'])
            u.set_password(request.POST['pwd'])
            u.save()
            t = TeacherInfo()
            t.name = request.POST['uname']
            t.email = request.POST['email']
            t.subject = request.POST['subject']
            t.classes = request.POST['classes']
            t.phone_number = request.POST['phno']
            t.save()
            messages.add_message(request, messages.SUCCESS, 'Registeration successful')
        except Exception:
            messages.add_message(request, messages.ERROR, 'A issue occur during registering')
        return render(request,'teacher_register.html')
    else:
        messages.add_message(request, messages.ERROR, '')
    return render(request, 'teacher_register.html')
def stud_reg(request):
    if request.method == 'POST':
        try:
            u = User()
            u.username = request.POST['uname']
            u.email = request.POST['email']
            u.password = request.POST['pwd']
            u.save()
            u = User.objects.get(username = request.POST['uname'])
            u.set_password(request.POST['pwd'])
            u.save()
            s = StudentInfo()
            s.name = request.POST['uname']
            s.email = request.POST['email']
            s.std = request.POST['std']
            s.class_section = request.POST['class']
            s.stream = request.POST['stream']
            s.rollno = request.POST['roll']
            messages.add_message(request, messages.SUCCESS, 'Registeration successful')
        except Exception:
            messages.add_message(request, messages.ERROR, 'A issue occur during registering')
        return render(request,'student_register.html')
    else:
        messages.add_message(request, messages.ERROR, '')
    return render(request, 'student_register.html')
def user_logout(request):
    logout(request)
    return redirect('home')

