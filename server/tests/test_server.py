from flask import url_for
from flask_testing import TestCase
from app import app
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://A_animal_api:5000/get_animal',text="tiger")
            mocker.get('http://A_country_api:5000/get_country',text="japan")
            mocker.post('http://A_winner_api:5000/get_winner',text="win")
            response= self.client.get(url_for("home"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"If a tiger fights in japan then they will win", response.data)