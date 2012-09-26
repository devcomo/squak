"""
Identity test fixtures
"""

from django.contrib.auth.models import User
from django.test import TestCase


class IdentityTestBase(TestCase):

    def create_user(self, **kwargs):

        if 'password' not in kwargs:
            kwargs.update({'password': 'pw'})

        if 'first_name' in kwargs:
            first_name = kwargs.pop('first_name')
        if 'last_name' in kwargs:
            last_name = kwargs.pop('last_name')

        user = User.objects.create_user(**kwargs)
        if first_name or last_name:
            user.first_name = first_name
            user.last_name = last_name
            user.save()

        return user

    def setUp(self):

        self.miles = self.create_user(
            username='miles',
            first_name='Miles',
            last_name='Davis',
            email='miles@example.com')

        self.trane = self.create_user(
            username='john',
            first_name='John',
            last_name='Coltrane',
            email='trane@example.com')

        self.bill = self.create_user(
            username='bill',
            first_name='Bill',
            last_name='Evans',
            email='bill@example.com')

        self.philly = self.create_user(
            username='phillyjoe',
            first_name='Philly',
            last_name='Joe Jones',
            email='phillyjoe@example.com')

        self.cannonball = self.create_user(
            username='cannonball',
            first_name='Cannonball',
            last_name='Adderley',
            email='cannonball@example.com')

        self.paul = self.create_user(
            username='paulchambers',
            first_name='Paul',
            last_name='Chambers',
            email='paulchambers@example.com')
