import unittest

from phonebook import PhoneBook

class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook('Allan', '0718150768')

    def test_add_contact(self):
        self.assertEqual(self.phonebook.add_contact(), '0718150768')

    def test_update_contact(self):
        self.phonebook.add_contact()
        updated_contact = self.phonebook.update_contact('Allan','0713803871')
        self.assertEqual(updated_contact,'0713803871')

    def test_delete_contact(self):
        self.phonebook.add_contact()
        self.assertTrue(self.phonebook.delete_contact('Allan'))