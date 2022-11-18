from django.shortcuts import render,redirect
from.forms import signupform
from django.contrib.auth import authenticate

# Create your views here.
def signup(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log')
    else:
        form = signupform()

    return render(request,'sign_up.html',{'form':form})

def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            Login(request)
            return render('next')
    else:
        return render(request,'login.html')

def next(request):
    return render(request,'next.html')