from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.conf import settings
from django.utils import timezone
from django.db.models import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
# from hrm import models as hrm_models
# from software_settings import models as settings_models


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have a email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create and save a super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_role = models.ForeignKey(
        'HRM.Designation', on_delete=models.CASCADE, default=None, blank=True, null=True)
    branch = models.ForeignKey(
        'HRM.Office', on_delete=models.CASCADE, default=None, blank=True, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of the user"""
        return self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email


class module(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """return string representation of our user"""
        return self.name
    

class sub_module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    module = models.ForeignKey(
        module, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        """return string representation of our user"""
        return self.module.name + ' - ' + self.name
