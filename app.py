"""
Phonebook app that adds, updates, deletes and view contacts
"""
class PhoneBook:
    def __init__(self, name, phone_number):
        self.username = name
        self.number = phone_number
        self.contacts = {}
    def add_contact(self):
        self.contacts[self.username] = self.number
        if self.contacts.get(self.username) is None:
            return False

        return True

    