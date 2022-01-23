from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


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
    projects = Project.objects.all() #TO get all data from database of projects
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)
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
    return render(request, 'projects/single-project.html', {'project':projectObj})
# Create your views here.

@login_required(login_url="login")     #If they are not loggedin they will be redirected to login page
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
       # print(request.POST)  # So we see its a dictionary of attributes of project and its details
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects') #user will be redirected to the projects page
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")     #If they are not loggedin they will be redirected to login page
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
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
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete_template.html', context)