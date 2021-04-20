import os 
from django.test import TestCase

from ..models import User

from .data import UserData as data

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email = 'example@email.com',
            first_name = 'Albert',
            surname = 'Einstein',
            birth_date = data.test_birth_date,
            avatar = data.test_photo,
            about_me = data.test_about_me,
            password = 'test_password123'
        )


    def test_str_method(self):
        print(self.user)
        # self.assertEqual(self.user.__str__(), self.user.email)

    # def test_email(self):
    #     self.assertEqual(self.user.email, 'example@enail.com')

    # def test_first_name(self):
    #     self.assertEqual(self.user.surname, 'Einstein')


    # def test_birth_date(self):
    #     self.assertEqual(self.user.birth_date, test_birth_date)


    # def test_avatar(self):
    #     self.assertEqual(self.user.avatar, test_photo_url)

    # def test_about_me(self):
    #     self.assertEqual(self.user.about_me, test_about_me)


    # def test_password(self):
    #     self.assertEqual(self.user.password, self.user.__class__.set_password('test_password123'))

