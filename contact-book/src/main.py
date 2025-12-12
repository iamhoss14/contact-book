from collections import defaultdict

class ContactBook:
    def __init__(self):
        self.contacts = defaultdict(dict)
    
    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
            return
        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email
        print(f"Contact '{name}' added successfully.")
    
    def view_contact(self, name):
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return
        contact = self.contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return
        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        print(f"Contact '{name}' updated successfully.")
    
    def delete_contact(self, name):
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return
        del self.contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    
if __name__ == "__main__":
    book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone (optional): ") or None
            email = input("Enter email (optional): ") or None
            book.add_contact(name, phone, email)
        
        elif choice == '2':
            name = input("Enter name to view: ")
            book.view_contact(name)
        
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to keep unchanged): ") or None
            email = input("Enter new email (leave blank to keep unchanged): ") or None
            book.update_contact(name, phone, email)
        
        elif choice == '4':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")