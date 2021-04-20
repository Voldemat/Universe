"""
    User global model
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .validators import image_max_resolution_validator, image_size_validator


class UserManager(BaseUserManager):
    def create_user(self, email:str = None, first_name:str = None, surname:str = None, birth_date:str = None, avatar:object = None, about_me:str = None, password:str = None):
        if not email:
            raise ValueError('Users must have an email address')


        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            surname = surname,
            birth_date = birth_date,
            avatar = avatar,
            about_me = about_me
        )
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, password = None):
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

    surname   = models.CharField('Surname', max_length = 255, blank = True, null = True)

    birth_date  = models.DateField('Birth date', blank = True, null = True)

    avatar      = models.ImageField(
        verbose_name    = 'Avatar',
        upload_to       = 'users/avatars/',
        blank           = True,
        null            = True
    )

    about_me    = models.CharField('About me', max_length = 1000, blank = True, null = True)

    is_active   = models.BooleanField(default = True)
    is_staff    = models.BooleanField(default = False)
    is_admin    = models.BooleanField(default = False)


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        print(self.email)
        return self.email

    def validate_image(image:object) -> None:
        image_max_resolution_validator(image, 500, 500)

        image_size_validator(image, 5.0)

        return None