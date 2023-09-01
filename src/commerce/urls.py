from django.urls import path
from commerce.views import welcome_page


urlpatterns = [
    path('', welcome_page, name='welcome_page'),
]