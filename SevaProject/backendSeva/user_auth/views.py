from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def user_login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Credentials Invalid")
            return redirect('user_login')
    else:
     return render(request,'user_login.html')

def user_signup(request):
    if request.method == 'POST':
         username=request.POST['username']
        #  firstname = request.POST['firstname']
        #  lastname = request.POST['lastname']
         email = request.POST['email']
         password = request.POST['password']
         password2 = request.POST['password2']
        #  address = request.POST['address']
        #  city = request.POST['city']
        #  state = request.POST['state']
        #  zip = request.POST['zip']
         
         if password==password2:
             if User.objects.filter(email=email).exists():
                 messages.info(request, 'Email Already Used')
                 return redirect('user_signup')
             elif User.objects.filter(username=username).exists():
                 messages.info(request, 'Useranme Already Used')
                 return redirect('user_signup')
             else:
                 user=User.objects.create_user(username=username,email=email,password=password)
                 user.save()
                 return redirect('user_login')
         else:
             messages.info(request, 'Password Not The Same')
             return redirect('user_signup')

    else:
      return render(request,'user_signup.html')


def register(request):
    return render(request,'register.html')



#def professional_signup(request):
 #   return render(request,'professional_signup.html')
