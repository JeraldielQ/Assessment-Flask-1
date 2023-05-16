import unittest
from app import app
from flask import session
from forex_python.converter import CurrencyRates, CurrencyCodes
from currency import CurrencyChecks

c = CurrencyRates(force_decimal=False)
cc = CurrencyCodes()


class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_home(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<div class="converter-form">', html)

    def test_conversion_same_currency(self):
        with self.client as client:
            self.assertEqual(c.convert("USD", "USD", 1), 1)
            self.assertEqual(c.convert("GBP", "GBP", 1), 1)
            self.assertEqual(c.convert("JPY", "JPY", 1), 1)
