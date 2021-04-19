"""
    User global model
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .validators import max_image_size


class UserManager(BaseUserManager):
    def create_user(self, email:str = None, first_name:str = None, last_name:str = None, birth_date:str = None, avatar:object = None, about_me:str = None, password:str = None):
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

    def create_superuser(self, email, password = None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.create_user(email, password)


        user.is_admin = True
        
        user.is_staff = True


        user.save(using = self._db)

        return user





class User(AbstractBaseUser):
    email       = models.EmailField(
        verbose_name    = 'Email Address',
        max_length      = 255,
        unique          = True
    )
    first_name  = models.CharField('First name', max_length = 255, blank = True, null = True)

    last_name   = models.CharField('Last name', max_length = 255, blank = True, null = True)

    birth_date  = models.DateField('Birth date', blank = True, null = True)

    avatar      = models.ImageField(
        verbose_name    = 'Avatar',
        upload_to       = 'users/avatars/',
        validators      = [max_image_size(300,300),],
        blank           = True,
        null            = True
    )

    about_me    = models.CharField('About me', max_length = 1000, blank = True, null = True)

    is_active   = models.BooleanField(default = True)
    is_staff    = models.BooleanField(default = False)
    is_admin    = models.BooleanField(default = False)


    objects = UserManager()