"""
Phonebook app that adds, updates, deletes and view contacts
"""
class Phonebook:
    def __init__(self):
        self.entries = {}
    
    def add(self, name, number):
        self.entries[name] = number
    
    def lookup(self, name):
        return self.entries[name]

    