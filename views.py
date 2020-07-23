from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Event
from django.http import HttpResponse


# Create your views here.
def index(request):
    dests = Event.objects.all()
    return render(request, "index.html", {'dests': dests})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect("/")

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['re-password']

        if password == password1:
            user = User.objects.create_user(username=username, password=password, email=email,
                                            first_name=first_name, last_name=last_name)
            user.save()
            print("User created")



        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')
