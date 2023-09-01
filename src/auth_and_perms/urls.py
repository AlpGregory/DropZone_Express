from django.urls import path
from auth_and_perms.views import signup_client, login


urlpatterns = [
    path('signup_client/', signup_client, name='signup_client'),
    path('login/', login, name='login'),
]