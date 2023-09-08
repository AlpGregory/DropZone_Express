from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_seller = models.BooleanField('Seller Account', default=False)
    is_client = models.BooleanField('Client Account', default=False)
    is_admin = models.BooleanField('Admin Account', default=False)

