from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app import models, forms


@login_required(login_url='/login/')
def add_client (request):
    if request.method == "GET":
        return render (request, "add_client.html")
	
    client_info = forms.ClientForm (request.POST)
    print "=================  " +str(client_info.is_valid()) + " ==================="
    client_info.save ()
    return redirect ("secure")
		
	
@login_required(login_url='/login/')
def secure_page (request):
    client_info = models.Client.objects.all ()
    r = dict()
    r["myform"] = client_info
    print dict(r)
    return render (request, "first_page.html", context=r)


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
            return redirect ("/secure")
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            messages.add_message(request, messages.ERROR, 'disabled account')

            pass
    else:
        # Return an 'invalid login' error message.
        print "user is None"
        messages.add_message(request, messages.ERROR, 'cant see it')
        pass
    return redirect ("/login")
    #return HttpResponse("POST ====== Welcome to Project KNIGHT /index ===== !")
