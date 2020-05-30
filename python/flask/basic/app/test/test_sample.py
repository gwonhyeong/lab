import os
import unittest

from flask_testing import TestCase
from manage import app


class TestSample(TestCase):

    def create_app(self):
        return app

    def test_sample(self):
        self.assertTrue(app.usercfg.version == 0.1)
