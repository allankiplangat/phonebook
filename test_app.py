import unittest
from app import Phonebook


class PhonebookTest(unittest.TestCase):
    def test_create_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Naomi", "0834557234")
        self.assertEqual("0834557234", phonebook.lookup("Naomi"))
