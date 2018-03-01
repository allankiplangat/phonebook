import unittest
import app

class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.phonebook = app.PhoneBook('Allan', '0718150768')

    def test_add_contact(self):
        self.assertTrue(self.phonebook.add_contact())