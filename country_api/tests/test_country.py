from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestHome(TestBase):
    def test_get_country(self):
        for i in range(20):    
            response= self.client.get(url_for("get_country"))
            self.assertIn(response.data.decode("utf-8"),["japan","france","brazil","russia","yemen"]) 