from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

def hello(request):
    return HttpResponse("Hello, world. You're at the Appli index.")

def accueil(request):
    return render(request, 'accueil.html', {'date': datetime.now()})

def log_out(request):
	logout(request)
	return redirect('login')
