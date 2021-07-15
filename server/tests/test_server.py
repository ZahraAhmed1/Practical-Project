from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home():
        with requests_mock.Mocker() as mocker:
            mocker.get('http://duel:5000/get_animal', text='hamster')
            mocker.get('http://duel:5000/get_country', text='Syria')
            mocker.post('http://duel:5000/get_winner', text='win')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)