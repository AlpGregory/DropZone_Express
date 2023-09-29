from django.db import models
from auth_and_perms.models import User


class Client(models.Model):
    first_name = models.CharField('First name', max_length=100, blank=False, null=False)
    last_name = models.CharField('Lastname', max_length=100, blank=False, null=False)
    address = models.TextField('Address', max_length=250, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.last_name
