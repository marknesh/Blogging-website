from app.models import Qoutes
import unittest

class quote_test(unittest.TestCase):
    def setUp(self):
        self.new_quote=Qoutes(id=1,quote="poa",author="at all")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Qoutes))





