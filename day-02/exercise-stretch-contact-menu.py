"Stretch Exercise: Contact Book Menu"

# Contact book using while loop
contact_book = {}

while True:
    print("====== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    # For display menue
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        name = input("Enter contact name: ").strip().title()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip().lower()

        contact_book[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Success: Contact '{name}' has been added!")

    elif choice == "2":
        search_name = input("Enter name to search: ").strip().title()

        if search_name in contact_book:
            details = contact_book[search_name]
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
        else:
            print("Error: Contact not found.")

    elif choice == "3":
        delete_name = input("Enter name to delete: ").strip().title()

        if delete_name in contact_book:
            del contact_book[delete_name]
            print(f"Success: '{delete_name}' deleted successfully.")
        else:
            print("Error: Contact does not exist.")

    elif choice == "4":
        if not contact_book:
            print("Your contact book is currently empty.")
        else:
            print("==== REGISTERED CONTACTS =====")
            for name, details in contact_book.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    elif choice == "5":
        print("Exiting...")
        break
