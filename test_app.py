import unittest
from app import Contact
class ContactTestCase(unittest.TestCase):
    def initial_setup(self):
        self.contact = Contact()