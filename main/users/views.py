from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'register.html', {'form':form})

def login(request):
    return render(request, 'login.html')