For templates of Apps we make template folder in project and project folder in templates
i.e.-> projects->template->project folder 
Here we can put our templates for the app

We use double curly braces to pass variables into the templates
{{  }}

We can access data (inside variables)using these double {{ }}.
{{ myobject.attribute }}
{{my_dict.key }}

{% and %} way of adding python like logic into

{% if user.is_authenictaed %}Hello, {{user.username}}.{% endif %}

So we use {} for tags and variables. Tags have some kind of logic , variables have output data






In models.py
We are going to create calsses that are going to represent tables.

When we create a class we have to inheit from models.Model to tell django its officialyy a model and not just a class.

When we create migration and run them, django is going to take thsi model and create a table.

After makemigration and migrate, in theory we should be able to see tables in admin panel.
But in actual admin panel is completely seperate thing. Its not directly tied to the database.
TO see changes, we need to register a model with the admin panel.

So in admin.py in projects->
#from .models import Project
#admin.site.register(Project)




FOreign Key establishes one to many relationships
