from django.contrib import admin
from django.urls import path, include
from django.conf import settings   # to get access to settings.py file to get access to MEDIA_ROOT and MEDIA_URL
from django.conf.urls.static import static  #static will help us create url for static files

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #This admin panel cannot be accessed until we have our database ready.
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), 
        name="reset_password"),

    # path('reset_password/', auth_views.PasswordResetView.as_view(), 
    #     name="reset_password"),


    # Mail for reset paswword has been sent from this link below
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),

    
    # This third link is the reset password, that the user of site has opened from mail
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name = "password_reset_confirm"),
    # <uidb64> -> encrypt userId in base 64 encryption

    # This last link tells us password was changed, i.e. password reset complete
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 1 - User submits email for reset             //PasswordResetView.as_view()             //name="reset_password"
# 2 - Email sent message                       //PasswordResetDoneView.as_view()         //name="password_reset_done"
# 3 = Email with link and reset instructions   //PasswordResetConfirmView                //name = "password_reset_confirm"
# 4 - Password successfully reset message      //PasswordResetCompleteView.as_view()     //name="password_reset_complete"