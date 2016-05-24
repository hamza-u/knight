from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def secure_page (request):
    return render (request, "first_page.html")
    #return HttpResponse("Welcome to Project KNIGHT. THIS IS SECURE PAGE!")


def welcome (request):
    return HttpResponse("Welcome to Project KNIGHT !")

def index(request):
    if request.method == "GET":
        return render (request, "registration/login.html")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        print "user is not None"
        if user.is_active:
            print "user is active"
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.
        print "user is None"
        pass
    return render (request, "first_page.html")
    #return HttpResponse("POST ====== Welcome to Project KNIGHT /index ===== !")
