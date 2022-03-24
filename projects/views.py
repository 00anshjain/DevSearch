from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from django.db.models import Q
# We dont need this here anymore, we import it in projects/utils.py file 
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm

from django.contrib import messages

from .utils import searchProjects, paginateProjects

# projectsList = [
#     {
#         'id': '1',
#         'title': "Ecommerce Website",
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': "Portfolio Website",
#         'description': 'This was a project where I built out my portfolio'
#     },
#     {
#         'id': '3',
#         'title': "Social Network",
#         'description': 'Awesome open source project I am still working on'
#     },  
# ]


def projects(request):
    # return render(request, 'projects/projects.html')
    # pass some msg
    # page = 'projects'
    # number = 10
    # context = {'page': page, 'number':number, 'projects':projectsList}
    # projects = Project.objects.all() #TO get all data from database of projects
    
    projects, search_query = searchProjects(request)
    # This searchProjects function is in projects/utils.py file
    
    # We want to set the paginator class for the results
    custom_range, projects = paginateProjects(request, projects, 6)
    # 6 results each time 



    context = {'projects':projects, 'search_query':search_query, 'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)
    # 'paginator':paginator, 
    # return render(request, 'projects/projects.html', {'page':page})
    # name for parameter is page


def project(request, pk): 
    # return HttpResponse('SINGLE PROJECT OF ' + str(pk))
    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    # return render(request, 'projects/single-project.html', {'project':projectObj, 'tags':tags})
    form = ReviewForm()

    if request.method == 'POST':

        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        # Update project Votecount

        projectObj.getVoteCount
        
        # This function will run, it will updtae and set vote count
        # We didnt have to call it like projectObj.getVoteCount() because we declared it as property 
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=projectObj.id)




    return render(request, 'projects/single-project.html', {'project':projectObj, 'form':form})
# Create your views here.

@login_required(login_url="login")     #If they are not loggedin they will be redirected to login page
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
       # print(request.POST)  # So we see its a dictionary of attributes of project and its details
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('account')
            # return redirect('projects') #user will be redirected to the projects page
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")     #If they are not loggedin they will be redirected to login page
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk) #project_set will give all the project of the user
    # It will ensure only owner can update the project
    # project = Project.objects.get(id=pk)

    form = ProjectForm(instance = project) #  Form will get all details of the project object taken to update
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project) #The request.POST data will be send to the project instance
        if form.is_valid():
            form.save() #IT will modify the project
            return redirect('projects') #user will be redirected to the projects page
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")     #If they are not loggedin they will be redirected to login page
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    # Only a logged in user, An owner of project can delete it
    # project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'delete_template.html', context)
    # delete_template.html is in templates outside project app. 