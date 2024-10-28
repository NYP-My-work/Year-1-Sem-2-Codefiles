from Monster import Monster

class FireMonster(Monster):
    def __init__(self,name="firebug",health=10,attack=9,defence=4,type="fire"):
        super().__init__(name, health, attack, defence,type)

def checker(instance):
    if (instance,FireMonster):
        print("This is a monster")
    else:
        print("This is not a monster")

Hello=FireMonster()
Hello.printname()
checker(Hello)