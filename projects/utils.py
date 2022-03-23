from .models import Project, Tag
from django.db.models import Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjects(request, projects, results) :
    # We want to set the paginator class for the results
    # page = 1
    page = request.GET.get('page')
    # results = 3
    # 3 results per page
    paginator = Paginator(projects, results)
    try:    
        projects = paginator.page(page)
    except PageNotAnInteger :
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    # We want our projects to get index by specific page and only have 3 results, intitally page 1
    # We want the page number to be changed manually from the front end
    # If no page found it will give exception PageNotAnInteger
    # If user goes to page that does not exist, it will give exception EmptyPage
    # So if user goes out of index, we give the last page
    # We will add page buttons in projects.html

    # custom_range = range(1, 20)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects


def searchProjects(request):

    search_query = '' # It will be passed by every filter we add
    # IF we dont have any data from front end we want it to be an empty string

    if request.GET.get('search_query'): # we check if we have any data for the query
        search_query = request.GET.get('search_query')  # If yes then we update search_query from blank string
    
    # We have to search project from tags
    tags = Tag.objects.filter(name__icontains=search_query)


    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        # We are going into parent object owner, and then we are gling into attribute of owner
        # i.e. name
        Q(tags__in=tags)
        # tags is many to many field in Projects, thast why we handled it differentely
        # Now we will see bunch of duplicates, agaian again and again printong because of tags
        #  So we add distinct
    )
    
    return projects, search_query