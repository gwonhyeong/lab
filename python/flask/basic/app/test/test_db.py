import os
import unittest

from flask_testing import TestCase

from manage import app

from app.main.model.user import User
from app.main.model.blacklist import Blacklist

class TestDB(TestCase):

    def create_app(self):
        return app

    def test_sample(self):
        users = User.query.all()
        blacklists = Blacklist.query.all()
        print(users, blacklists)
        self.assertTrue(app.usercfg.version == 0.1)
