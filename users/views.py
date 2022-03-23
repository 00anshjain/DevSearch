from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile, Skill
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .utils import searchProfiles, paginateProfiles

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
            return redirect('edit-account')
            # return redirect('profiles')
        else:
            messages.success(request, 'An error has occurred during registration')

    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)



def profiles(request):
    
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 3)

    context = {'profiles': profiles, 'search_query' : search_query, 'custom_range':custom_range}
    # We pass search query as when we search anything, we want it to show in the space provided
    # Otherwise it will disappear
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile':profile, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    # topSkills = profile.skill_set.exclude(description__exact="")
    # otherSkills = profile.skill_set.filter(description="")
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills':skills, 'projects': projects}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)
    # As we update profile, user details will also be updated, we have used signals for this

@login_required(login_url='login')
def createSkill(request):
    form = SkillForm()
    profile = request.user.profile
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit = False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance = skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)
    

def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    context = {'object': skill}
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')
    return render(request, 'delete_template.html', context)