class Player():
    def __init__(self,name):
        self.__name=name
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    

class BasketBall(Player):
    positions=["Guard","Foward","Center"]
    def __init__(self, name,postition):
        super().__init__(name)
        self.__postition=postition
        self.position_checker
    def get_pos(self):
        return self.__postition
    def set_pos(self,postitions):
        self.__postition=postitions
        self.position_checker()
    def position_checker(self):
        if self.get_pos not in  self.positions:
            print("Invalid Postition!")
            self.__postition=""
    def __str__(self):
        to_print=f"{self.get_name} playing as a {self.get_pos}"
        return to_print

basketball_name=input("input team name!")
for i in range(1,6):
    name=input("Enter player name: ")
    position_input=input("Enter posititon name: ")
    player=BasketBall(name,position_input)
