class Salesperson:
    def __init__(self,name,commission):
        self.__name=None
        self.__commission=0
    def set_name(self,new_name):
        self.__name=new_name
    def get_name(self):
        return self.__name
    
    def salesperson_commission(self,payment_recevied):
        return 0.01*float(payment_recevied)*2.00
    
    def __str__(self):
        return f"{self.salesperson_commission(0),self.get_name()}"

nameinput=input("Enter name:")
comissioninput=input("Enter payment recevied:")
customer1=Salesperson(nameinput,comissioninput)

customer1.set_name(nameinput)
customer1.salesperson_commission(comissioninput)

print(customer1)