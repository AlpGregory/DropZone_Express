from django.urls import path
from django.contrib.auth.decorators import login_required
from commerce.views import welcome_page


urlpatterns = [
    path('', login_required(welcome_page), name='welcome_page'),
]