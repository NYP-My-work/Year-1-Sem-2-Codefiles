class Customer:
    def __init__ (self,name,email,moblie_number):
        self.name=name
        self.email=email
        self.moblie_number=moblie_number
    def get_customer_info(self):
        return f"Name: {self.name}, Email: {self.email},Moblie Number: {self.moblie_number}"
    
customer1=Customer("John Doe","JD@gmail.com","12345678")
print(customer1.get_customer_info())
