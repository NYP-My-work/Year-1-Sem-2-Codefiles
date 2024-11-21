# Phone class definition
class Phone:
    def __init__(self, make, model, price):
        self._id = None  # Initialize id to None
        self._make = make
        self._model = model
        self._price = price
    
    # Accessor methods
    @property
    def id(self):
        return self._id
    
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def price(self):
        return self._price
    
    # Mutator methods
    @id.setter
    def id(self, value):
        self._id = value
    
    @make.setter
    def make(self, value):
        self._make = value
    
    @model.setter
    def model(self, value):
        self._model = value
    
    @price.setter
    def price(self, value):
        self._price = value
    
    def __str__(self):
        return f"ID: {self._id}, Make: {self._make}, Model: {self._model}, Price: ${self._price:.2f}"

class PhoneShelve:
    def __init__(self, filename="phone_inventory.db"):
        self.filename = filename
        self.current_id = 0
        
    def __enter__(self):
        import shelve
        self.db = shelve.open(self.filename)
        # Initialize current_id based on existing entries
        if 'current_id' in self.db:
            self.current_id = self.db['current_id']
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db['current_id'] = self.current_id
        self.db.close()
        
    def search(self, search_term):
        try:
            results = []
            for key in self.db:
                if key != 'current_id':  # Skip the counter
                    phone = self.db[key]
                    if (search_term.lower() in phone.make.lower() or 
                        search_term.lower() in phone.model.lower() or
                        search_term == str(phone.id)):
                        results.append(phone)
            return results
        except Exception as e:
            raise Exception(f"Error searching for phone: {str(e)}")

    def add(self, phone):
        try:
            self.current_id += 1
            phone.id = self.current_id
            self.db[str(phone.id)] = phone
            return phone.id
        except Exception as e:
            raise Exception(f"Error adding phone: {str(e)}")

    def update(self, phone_id, make, model, price):
        try:
            if str(phone_id) in self.db:
                phone = self.db[str(phone_id)]
                phone.make = make
                phone.model = model
                phone.price = price
                self.db[str(phone_id)] = phone
                return True
            return False
        except Exception as e:
            raise Exception(f"Error updating phone: {str(e)}")

    def delete(self, phone_id):
        try:
            if str(phone_id) in self.db:
                del self.db[str(phone_id)]
                return True
            return False
        except Exception as e:
            raise Exception(f"Error deleting phone: {str(e)}")

    def display_all(self):
        try:
            phones = []
            for key in self.db:
                if key != 'current_id':  # Skip the counter
                    phones.append(self.db[key])
            return phones
        except Exception as e:
            raise Exception(f"Error displaying phones: {str(e)}")

def display_menu():
    print("\nPhone Inventory System")
    print("1. Search for a phone")
    print("2. Add a new phone")
    print("3. Update a phone")
    print("4. Delete a phone")
    print("5. Display all phones")
    print("6. Quit")
    return input("Enter your choice (1-6): ")

def main():
    with PhoneShelve() as shelve:
        while True:
            choice = display_menu()
            
            try:
                if choice == '1':
                    search_term = input("Enter search term: ")
                    results = shelve.search(search_term)
                    if results:
                        for phone in results:
                            print(phone)
                    else:
                        print("No phones found.")

                elif choice == '2':
                    make = input("Enter make: ")
                    model = input("Enter model: ")
                    while True:
                        try:
                            price = float(input("Enter price: "))
                            break
                        except ValueError:
                            print("Please enter a valid price.")
                    phone = Phone(make, model, price)
                    phone_id = shelve.add(phone)
                    print(f"Phone added with ID: {phone_id}")

                elif choice == '3':
                    while True:
                        try:
                            phone_id = int(input("Enter phone ID to update: "))
                            break
                        except ValueError:
                            print("Please enter a valid ID.")
                    make = input("Enter new make: ")
                    model = input("Enter new model: ")
                    while True:
                        try:
                            price = float(input("Enter new price: "))
                            break
                        except ValueError:
                            print("Please enter a valid price.")
                    if shelve.update(phone_id, make, model, price):
                        print("Phone updated successfully.")
                    else:
                        print("Phone not found.")

                elif choice == '4':
                    while True:
                        try:
                            phone_id = int(input("Enter phone ID to delete: "))
                            break
                        except ValueError:
                            print("Please enter a valid ID.")
                    if shelve.delete(phone_id):
                        print("Phone deleted successfully.")
                    else:
                        print("Phone not found.")

                elif choice == '5':
                    phones = shelve.display_all()
                    if phones:
                        for phone in phones:
                            print(phone)
                    else:
                        print("No phones in inventory.")

                elif choice == '6':
                    print("Thank you for using Phone Inventory System!")
                    break

                else:
                    print("Invalid choice. Please try again.")

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Please try again.")

if __name__ == "__main__":
    main() 