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
    
    def update_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        return self.contacts.get(name)

    def delete_contact(self, name):
        if self.contacts[name]:
            del self.contacts[name]
        else:
            raise KeyError
        if name in self.contacts:
            return False
        return True

    