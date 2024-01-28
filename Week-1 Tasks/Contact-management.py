import os
import json

Contacts_saved_file = "contacts.txt"

# Load contacts from the text file 
def load_contacts():
    contacts = []
    if os.path.exists(Contacts_saved_file):
        with open(Contacts_saved_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, phone = line.strip().split(',')
                contacts.append({"name": name, "phone": phone})
    return contacts

# Save contacts to the text file
def save_contacts(contacts):
    with open(Contacts_saved_file, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

def add_contact(contacts, name, phone):
    if not name or not phone:
        print("Name and phone number are required.")
        return

    for contact in contacts:
        if contact['name'] == name:
            print(f"Contact with the name {name} already exists.")
            return

    contacts.append({"name": name, "phone": phone})
    print(f"Contact {name} added successfully!")
    save_contacts(contacts)  # Save contacts after adding a new one

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"{contact['name']}: {contact['phone']}")

def search_contact(contacts, name):
    found = False
    for contact in contacts:
        if contact['name'] == name:
            print(f"Contact: {contact['name']}, Phone: {contact['phone']}")
            found = True
            break

    if not found:
        print(f"No contact found with the name {name}.")

def update_contact(contacts, name):
    found = False
    for contact in contacts:
        if contact['name'] == name:
            print(f"Current contact information for {name}: {contact['phone']}")
            new_phone = input(f"Enter the new phone number for {name}: ")
            contact['phone'] = new_phone
            print(f"Contact information for {name} updated successfully!")
            found = True
            break

    if not found:
        print(f"No contact found with the name {name}.")

def main():
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter the contact name: ").strip().capitalize()
            phone = input("Enter the phone number: ").strip()
            add_contact(contacts, name, phone)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            name = input("Enter the contact name to search: ").strip().capitalize()
            search_contact(contacts, name)
        elif choice == '4':
            name = input("Enter the contact name to update: ").strip().capitalize()
            update_contact(contacts, name)
        elif choice == '5':
            save_contacts(contacts)  # Save contacts before exiting
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
