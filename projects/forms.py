from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm): #This now makes it model form
    # We will import it form the inherited Model Form
    class Meta:
        model = Project
        # field = ['title', ]    we can create a list like this else
        # fields = '__all__'
        # FOr all, it will generate field for every attribut of project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        # ID and created time will not be there because that are automatically generated

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})
        # self.fields['title'].widget.attrs.update({'class':'input'})

        # self.fields['description'].widget.attrs.update({'class':'input'})


