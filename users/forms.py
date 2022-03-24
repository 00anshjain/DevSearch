from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
# This CustomUserCreationForm is inherited from UserCreationForm.
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        # password1 is password and password2 is renter password rfor comfirmation, Its given in django documentation
        labels = {
            'first_name' : 'Name',
        }
        # So first name will be named as name in form on screen


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # We loop through all the fields of input and add class input to it
        # Class we have use to apply css, we cant do it in HTML file BEcause we
        # have used for loop there so we cant access all fileds and apply class to each one of it



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 
        'location', 'bio', 'short_intro', 'profile_image', 
        'social_github', 'social_linkedin', 'social_twitter', 
        'social_youtube', 'social_website']


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude =['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
