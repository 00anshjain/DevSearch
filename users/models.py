from django.db import models
from django.contrib.auth.models import User  # user used by django for authetication and login in admin page
# check django user model for more information
# Create your models here.
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    # ANytime user is deleted the profile is deleted
    name = models.CharField(max_length=200, blank = True, null = True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank = True, null = True)
    location = models.CharField(max_length=200, blank = True, null = True)
    short_intro = models.CharField(max_length=200, blank = True, null = True)
    bio = models.TextField(blank = True, null = True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    # We want specifically a folder for profile pictures. SO in static in mages we create a new folder here
    # static->images->profiles
    social_github = models.CharField(max_length=200, blank = True, null = True)
    social_twitter = models.CharField(max_length=200, blank = True, null = True)
    social_linkedin = models.CharField(max_length=200, blank = True, null = True)
    social_youtube = models.CharField(max_length=200, blank = True, null = True)
    social_website = models.CharField(max_length=200, blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key = True, editable = False)
    

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length=200, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key = True, editable = False)
    def __str__(self):
        return str(self.name)

# @receiver(post_save, sender=Profile)
# def createProfile(sender, instance, created, **kwargs):
#     print('Profile Saved!')
#     print('Instance:', instance)
#     print('CREATED:', created)

# def deleteUser(sender, instance, **kwargs):
#     print('Deleting User...')


# post_save.connect(createProfile, sender=User)
# # here sender will be user anytime user model is created, a profile will be created

# post_delete.connect(deleteUser, sender=Profile)

 
# def createProfile(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user = user,
#             username = user.username,
#             email=user.email,
#             name=user.first_name,
#         )

# def deleteUser(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()
    


# post_save.connect(createProfile, sender=User)



# post_delete.connect(deleteUser, sender=Profile)

