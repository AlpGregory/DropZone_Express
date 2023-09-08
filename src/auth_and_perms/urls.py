from django.urls import path
from auth_and_perms.views import (signup, client_signup, seller_signup,
                                  admin_signup, login)


urlpatterns = [
    path('signup', signup, name='signup'),
    path('signup/client/', client_signup, name='client_signup'),
    path('signup/seller/', seller_signup, name='seller_signup'),
    path('signup/admin', admin_signup, name='admin_signup'),
    path('login/', login, name='login'),
]
