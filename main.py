from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
              raise ValueError ("Ім’я не може бути порожнім")
        super().__init__(value)

        

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
             raise ValueError("Номер телефону має містити 10 цифр")
        super().__init__(value)



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
         self.phones.append(Phone(phone))

    def remove_phone(self, phone):
         self.phones = [p for p in self.phones if p.value != phone]

    def find_phone(self,phone):
         for p in self.phones:
              if p.value == phone:
                   return p
        
         return None

    def edit_phone(self, old_phone, new_phone):
         for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
         return False
         

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value]=record

    def find_record(self, name):
        return self.data.get(name)

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
                
