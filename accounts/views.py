from django.shortcuts import render, redirect

# Create your views here.
def register(request):
        
    template = 'accounts/register.html'
    context = {
    }
    if request.method == 'POST':
        # TODO Register User
        return
    else:
        return render(request, template, context)

def login(request):
    template = 'accounts/login.html'
    context = {
    }
    if request.method == 'POST':
        # TODO Login User
        return
    else:
        return render(request, template, context)
    
def logout(request):
    return redirect('index')
    
def dashboard(request):
    template = 'accounts/dashboard.html'
    context = {
    }
    return render(request, template, context)