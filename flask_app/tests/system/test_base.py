from unittest import TestCase
from flask_app.app import app


class BaseTest(TestCase):

    def setUp(self) -> None:
        # with inheritence mechanism i will use self.app() in the place of app.test_client()
        self.app = app.test_client
        app.testing = True
