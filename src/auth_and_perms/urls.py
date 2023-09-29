from django.urls import path
from auth_and_perms.views import (signup, ClientSignUpView, seller_signup,
                                  admin_signup, login_view)


urlpatterns = [
    path('signup', signup, name='signup'),
    path('signup/client/', ClientSignUpView.as_view(), name='client_signup'),
    path('signup/seller/', seller_signup, name='seller_signup'),
    path('signup/admin', admin_signup, name='admin_signup'),
    path('login/', login_view, name='login'),
]
