from django.db import models
from django.contrib import auth
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        # auth.models.User has attribute username to get user's name
        return "@{}".format(self.username)
