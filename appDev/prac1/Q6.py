from Q4 import * 

class Salesperson(Phone):
    def __init__(self,name,commission,make,model,price,phone):
        self.__name=None
        self.__commission=0
        self.__phone=None
        super().__init__(make,model,price)

    def set_name(self,new_name):
        self.__name=new_name
    def get_name(self):
        return self.__name
    
    def salesperson_commission(self,payment_recevied):
        return 0.01*float(payment_recevied)*2.00
    
    def salesperson_sold(self,phone):
        self.__phone=phone
    def __str__(self):
        return f"{self.get_Phone_info}"