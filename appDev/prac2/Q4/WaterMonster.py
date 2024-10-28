from Monster import Monster

class WaterMonster(Monster):
    def __init__(self,name="Waterbird",health=15,attack=6,defence=3,type="Water"):
        super().__init__(name, health, attack, defence,type)

def checker(instance):
    if (instance,WaterMonster):
        print("This is a monster")
    else:
        print("This is not a monster")

Hello=WaterMonster()
Hello.printname()