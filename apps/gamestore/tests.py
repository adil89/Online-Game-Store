from django.test import TestCase, Client
from django.db import models
import unittest

from .models import Game, Profile, Transaction, Score

# TODO: Divide the tests to smaller modules
class BasicGameTestCase(TestCase):
    """TODO"""
    def setup(self):
        self.client = Client()
        # TODO init db with mock data

class BasicProfileTestCase(TestCase):
    """TODO"""
    pass

class BasicTransactionTestCase(TestCase):
    """TODO"""
    pass

class BasicScoreTestCase(TestCase):
    """TODO"""
    pass
