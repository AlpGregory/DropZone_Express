from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('Email Address', primary_key=True)
    is_supplier = models.BooleanField('Supplier', default=False)

