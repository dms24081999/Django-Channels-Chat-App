from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    count=User.objects.count()
    return render(request,'home.html',{
        'user_count':count
    })



@login_required(login_url='account_login')
def secret_page(request):
    return render(request,'secret_page.html')




