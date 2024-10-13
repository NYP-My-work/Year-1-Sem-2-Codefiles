class Phone:
    def __init__(self,make,model,price):
        self.make=make
        self.model=model
        self.price=price
    def get_Phone_info(self):
        return f"Make: {self.make},Model: {self.model}, Price: {self.price}"

stopper=True
while stopper:
    Make_input=input("Enter the make of the phone: ( Enter Exit to exit )  ")
    if Make_input=="Exit":
        stopper=False
    Model_input=input("Enter the model of the phone: ")
    Price_input=input("Enter the price of the phone: ")
    
    phoneinputt=Phone(Make_input,Model_input,Price_input)
    print(phoneinputt.get_Phone_info())
