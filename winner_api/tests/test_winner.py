from flask import url_for
from flask_testing import TestCase
from app import app
import random

class TestBase(TestCase):
    def create_app(self):
        return app
        
class TestHome(TestBase):
    def test_get_winner(self):
        test_cases={"animal":random.choice(["bear","fish","cat","tiger"]) , "country":random.choice(["japan","france","brazil","russia","yemen"])}
        for i in range(20):    
            response= self.client.post(url_for("get_winner"),json=test_cases)
            self.assertIn(response.data.decode("utf-8"),["win","lose"])