import shelve

# Define the Phone class
class Phone:
    def __init__(self, id=None, make=None, model=None, price=None):
        self.id = id
        self.make = make
        self.model = model
        self.price = price

    # Accessors
    def get_id(self):
        return self.id

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    # Mutators
    def set_id(self, id):
        self.id = id

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Make: {self.make}, Model: {self.model}, Price: {self.price}"


# Add a new phone
def add_phone(shelf):
    try:
        id = input("Enter phone id: ")
        if id in shelf:
            print("Phone with this ID already exists.")
            return
        make = input("Enter phone make: ")
        model = input("Enter phone model: ")
        price = input("Enter price of phone: ")

        phone = Phone(id, make, model, price)
        shelf[id] = phone
        print("Phone added successfully.")
    except Exception as e:
        print(f"Error adding phone: {e}")


# Search for a phone
def search_phone(shelf):
    try:
        id = input("Enter phone id to search: ")
        if id in shelf:
            print(shelf[id])
        else:
            print("Phone not found.")
    except Exception as e:
        print(f"Error searching phone: {e}")


# Update phone details
def update_phone(shelf):
    try:
        id = input("Enter the phone id to update: ")
        if id in shelf:
            phone = shelf[id]
            new_make = input("Enter new make (Leave empty to remain unchanged): ")
            new_model = input("Enter new model (Leave empty to remain unchanged): ")
            new_price = input("Enter new price (Leave empty to remain unchanged): ")

            if new_make:
                phone.set_make(new_make)
            if new_model:
                phone.set_model(new_model)
            if new_price:
                phone.set_price(new_price)

            shelf[id] = phone
            print("Phone updated successfully.")
        else:
            print("Phone not found.")
    except Exception as e:
        print(f"Error updating phone: {e}")


# Delete a phone
def delete_phone(shelf):
    try:
        id = input("Enter the phone id to delete: ")
        if id in shelf:
            del shelf[id]
            print("Phone deleted successfully.")
        else:
            print("Phone not found.")
    except Exception as e:
        print(f"Error deleting phone: {e}")


# Display all phones
def display_all_phones(shelf):
    try:
        if len(shelf) == 0:
            print("No phones in inventory.")
        else:
            for phone in shelf.values():
                print(phone)
    except Exception as e:
        print(f"Error displaying phones: {e}")


# Display menu
def display_menu():
    print("\nSelect the program (1-6) to run:")
    print("1. Search for a phone")
    print("2. Add a new phone")
    print("3. Update phone details")
    print("4. Delete a phone")
    print("5. Display all phones")
    print("6. Quit the program")


# Main program
def main():
    with shelve.open("phone_inventory") as shelf:
        while True:
            display_menu()
            choice = input("Enter your command (1-6): ")

            if choice == "1":
                search_phone(shelf)
            elif choice == "2":
                add_phone(shelf)
            elif choice == "3":
                update_phone(shelf)
            elif choice == "4":
                delete_phone(shelf)
            elif choice == "5":
                display_all_phones(shelf)
            elif choice == "6":
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")


# Run the program with exception handling
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
