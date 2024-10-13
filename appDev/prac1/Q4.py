class Phone:
    def __init__(self,make,model,price):
        self.__make=None
        self.__model=None
        self.__price=None
    
    def set_make(self,new_make):
        self.__make=new_make

    def get_make(self):
        return f"The name is {self.__make}"
    
    def set_model(self,new_model):
        self.__model=new_model

    def get_model(self):
        return f"The email is {self.__model}"
    
    def set_price(self,new_price):
        self.__price=new_price

    def get_price(self):
        return f"The phone number is {self.__price}"
    
    def get_Phone_info(self):
        return f"Make: {self.get_make()},Model: {self.get_model()}, Price: {self.get_price()}"



Make_input=input("Enter the make of the phone: ( Enter Exit to exit )  ")
Model_input=input("Enter the model of the phone: ")
Price_input=input("Enter the price of the phone: ")
if Price_input.isnumeric()==False:
    Price_input=0
    
phoneinputt=Phone(Make_input,Model_input,Price_input)
phoneinputt.set_make(Make_input)
phoneinputt.set_model(Model_input)
phoneinputt.set_price(Price_input)
print(phoneinputt.get_Phone_info())
