class PhoneBook:
    def __init__(self, name, phone_number):
        self.username = name
        self.number = phone_number
        self.contacts = {}
    
    def add_contact(self):
        self.contacts[self.username] = self.number

        if self.username not in self.contacts:
            return "Your contacts could not be added."
        
        return self.contacts[self.username]
    