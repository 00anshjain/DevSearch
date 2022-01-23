from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method=='POST': 
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        # when user enters these we want to check data if something goes wrong
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        # authenticate will check if the password mathces with username, it will either return user instance or none

        if user is not None:
            login(request, user)
            # print('login successful')
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request) #It will delete that session
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    # form = UserCreationForm()
    form = CustomUserCreationForm
    #print("hello")
    if request.method=='POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        
        # ek baar register krna
        if form.is_valid():
            user = form.save(commit=False)
            # Commit false, we get the instance and we can edit it
            user.username = user.username.lower() #TO make all in lowercase
            user.save()
            print('Kachra')
            messages.success(request, 'User account was created!')
            
            login(request, user)     # We got this user instance because of commit=false and now we are using it
            return redirect('profiles')
        else:
            messages.success(request, 'An error has occurred during registration')

    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)



def profiles(request):
    profile = Profile.objects.all()
    context = {'profiles': profile}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile':profile, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)