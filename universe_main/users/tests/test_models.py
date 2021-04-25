import uuid

from django.test import TestCase

from ..models import User

from .data import user_data as data


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**data)


    def test_str_method(self):
        self.assertEqual(self.user.__str__(), self.user.email)

    def test_email(self):
        self.assertEqual(self.user.email, data['email'])

    def test_first_name(self):
        self.assertEqual(self.user.surname, data['surname'])


    def test_birth_date(self):
        self.assertEqual(self.user.birth_date, data['birth_date'])


    def test_about_me(self):
        self.assertEqual(self.user.about_me, data['about_me'])


    def test_password(self):
        self.assertTrue(self.user.check_password(data['password']))

