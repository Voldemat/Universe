"""
    User global model
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .validators import max_image_size

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, birth_date, avatar, about_me, password = None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            birth_date = birth_date,
            avatar = avatar,
            about_me = about_me
        )
        user.set_password(password)
        user.save(using = self._db)

        return user





class User(AbstractBaseUser):
    email       = models.EmailField(
        verbose_name    = 'Email Address',
        max_length      = 255,
        unique          = True
    )
    first_name  = models.CharField('First name', max_length = 255, blank = True)

    last_name   = models.CharField('Last name', max_length = 255, blank = True)

    birth_date  = models.DateField('Birth date', blank = True)

    avatar      = models.ImageField(
        verbose_name    = 'Avatar',
        upload_to       = 'users/avatars/',
        validators      = [max_image_size(300,300),],
        blank           = True
    )

    about_me    = models.CharField('About me', max_length = 1000, blank = True)

    is_active   = models.BooleanField(default = True)
    is_staff    = models.BooleanField(default = False)
    is_admin    = models.BooleanField(default = False)
