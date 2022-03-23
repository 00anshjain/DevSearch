# FOr helper functions that we create, not to mess up views
from django.db.models import Q
from .models import Profile, Skill

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results) :
    # We want to set the paginator class for the results
    # page = 1
    page = request.GET.get('page')
    # results = 3
    # 3 results per page
    paginator = Paginator(profiles, results)
    try:    
        profiles = paginator.page(page)
    except PageNotAnInteger :
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
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

    return custom_range, profiles


def searchProfiles(request):

    search_query = '' # It will be passed by every filter we add
    # IF we dont have any data from front end we want it to be an empty string

    if request.GET.get('search_query'): # we check if we have any data for the query
        search_query = request.GET.get('search_query')  # If yes then we update search_query from blank string

    # print('SEARCH: ', search_query)

    # profile = Profile.objects.filter(name__icontains = search_query)
    # icontains for not case sensitive

    # profile = Profile.objects.filter(name__icontains = search_query, short_intro__icontains =search_query)
    # Now problem with this is our profile should contain both this short intro value and name value
    # All fields have to have that value when we use comma in between
    
    # So we use Q look up, we say look up either by the name or short_intro

    # profile = Profile.objects.filter(
    #     Q(name__icontains = search_query) | Q(short_intro__icontains =search_query)
    # )

    #  We could either use '&' or '|'


    # Now we will search developers by their skills
    #  Thats totally different because this isnt attribute of developer, its a child object
    # with entirely differnet  table in the database
    
    #So we need to search the profile and skills together and see if profile contaisn one of these skills 
    #     

    # skills = Skill.objects.filter(name__iexact=search_query)
    skills = Skill.objects.filter(name__icontains=search_query)
    # SO we will get many skills and we want to search if the profile we are search have one of those skills
    # profile = Profile.objects.filter(
    #     Q(name__icontains = search_query) |
    #     Q(short_intro__icontains =search_query) | 
    #     Q(skill__in=skills)
    # )
    # skill__in=skills -> does the profile have skill that is listed in skills
    # Problem with above is we are getting many duplicates
    #  We getting duplicates, because of skills, there are multiple skills

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains = search_query) |
        Q(short_intro__icontains =search_query) | 
        Q(skill__in=skills)
    )
    #  Now we get one instance of each user



    return profiles, search_query
