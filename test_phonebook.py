import unittest

from phonebook import PhoneBook

class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook('Allan', '0718150768')

    def test_add_contact(self):
        self.assertEqual(self.phonebook.add_contact(), '0718150768')