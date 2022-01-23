from django.db import models
import uuid
from users.models import Profile
from uuid import uuid4
# Create your models here.
def generateUUID():
    return str(uuid4())

class Project(models.Model):
    owner = models.ForeignKey(Profile, null = True, blank = True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank=True) #we can have no data in this
    # null is for database, blank is for django to know to accept blank values in form
    featured_image = models.ImageField(null = True, blank=True, default="default.jpg")
    # ANy model we dont add image for will have this default picture until we don't modify it
    demo_link = models.CharField(max_length = 2000, null = True, blank = True)
    source_link = models.CharField(max_length = 2000, null = True, blank = True)
    tags = models.ManyToManyField('Tag', blank = True)
    vote_total = models.IntegerField(default = 0, null = True, blank = True)
    vote_ratio = models.IntegerField(default = 0, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key = True, editable = False)
    # id = models.UUIDField(default=generateUUID, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.title
    #So that we can see title of project in table



class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    # owner =
    project= models.ForeignKey(Project, on_delete= models.CASCADE)
    # OnDelete is what will hapeen to review wqhen project is deleted. IF on_delete = models.SET_NULL, then if the project is deleted, the reviews for that would be set NULL
    # if  on_delete= models.CASCADE, then on deleting project, all reviews for it will also be deleted
    body = models.TextField(null = True, blank = True)  #This if for many to many relationships
    value = models.CharField(max_length = 200, choices = VOTE_TYPE) 
    # Now its gonna be drop down list for value
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key = True, editable = False)
    # id = models.UUIDField(default=generateUUID, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length =200)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key = True, editable = False)
    # id = models.UUIDField(default=generateUUID, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.name


