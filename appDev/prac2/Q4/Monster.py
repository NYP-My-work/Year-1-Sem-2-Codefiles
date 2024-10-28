class Monster():
    def __init__(self,name,health,attack,defence,type):
        self.__name=name
        self.__health=health
        self.__attack=attack
        self.__defence=defence
        self.__type=type
    def get_name(self):
        return self.__name 
    def get_type(self):
        return self.__type
    def get_health(self):
        return self.__health
    def get_attack(self):
        return self.__attack
    def get_defence(self):
        return self.__defence
    def printname(self):
        print(f"{self.__name } is a {self.__type} monster")
    
    