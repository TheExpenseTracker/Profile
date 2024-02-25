
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    # path('',views.index , name='index')
    path('',views.homepage, name=""),

    path('register',views.register, name="register"),

    path('my_login',views.my_login, name="my_login"),
    path('my_logout',views.my_logout, name="my_logout"),
    path('account',views.accountSettings,name="account"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('user',views.userPage, name='user'),

    path('reset_password',
     auth_views.PasswordResetView.as_view(template_name="authenticate/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent', 
     auth_views.PasswordResetDoneView.as_view(template_name="authenticate/password_reset_sent.html"), 
     name="password_reset_done"),

    path('reset/<uidb64>/<token>', 
         auth_views.PasswordResetConfirmView.as_view(template_name="authenticate/password_reset_form.html"), 
         name="password_reset_confirm"),

    path('reset_password_complete', 
         auth_views.PasswordResetCompleteView.as_view(template_name="authenticate/password_reset_done.html"), 
         name="password_reset_complete"),
]