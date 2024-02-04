from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User, Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
@admin_only
def hod(request):
    return render(request, 'loginApp/hod.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff(request):
    return render(request, 'loginApp/staff.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['STUDENT'])
def student(request):
    return render(request, 'loginApp/student.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # throw message when any fields are wrong while registering
            username = form.cleaned_data.get('username')

            # below commented code is for adding registered user to STUDENT group automatically, smae can do with signals.py
            # user = form.save()
            # username = form.cleaned_data.get('username')
            # group = Group.objects.get(name='STUDENT')
            # user.groups.add(group)

            messages.success(request,"Account created for "+ username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'loginApp/register.html', context)

@unauthenticated_user
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username,password)
        if User.objects.filter(username=username).exists():
            #user exist in User's authenticate password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('hod')
            else:
                messages.info(request, "Password is not Valid")
        else:
            ##user NOT exist in users print username not exist.
            print("No user")
            messages.info(request, "Username does not exist")
            #return render(request, 'loginApp/login.html')
    return render(request, 'loginApp/login.html')

def userlogout(request):
    logout(request)
    return redirect('login')
