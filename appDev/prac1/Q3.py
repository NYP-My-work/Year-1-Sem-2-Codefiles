class Customer:
    def __init__(self,email,name,moblie_no):
        self.__email=None
        self.__name=None
        self.__moblie_no=None
    def set_name(self,new_name):
        self.__name=new_name

    def get_name(self):
        return f"The name is {self.__name}"
    
    def set_email(self,new_email):
        self.__email=new_email

    def get_email(self):
        return f"The name is {self.__email}"
    
    def set_moblie(self,new_moblie):
        self.__moblie_no=new_moblie

    def get_moblie(self):
        return f"The name is {self.__moblie_no}"
    
    
Name_input=input("Enter your name: ")
Moblie_input=input("Enter your moblie: ")
Email_input=input("Enter your email: ")

customer1=Customer(Name_input,Moblie_input,Email_input)
customer1.set_name(Name_input)
customer1.set_email(Email_input)
customer1.set_moblie(Moblie_input)

print(customer1.get_name())
print(customer1.get_moblie())
print(customer1.get_email())