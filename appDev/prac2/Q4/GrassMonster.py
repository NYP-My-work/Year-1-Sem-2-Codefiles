from Monster import Monster

# GrassMonster class inheriting from Monster
class GrassMonster(Monster):
    def __init__(self, name="Grasshopper", health=20, attack=5, defence=3,type="Grass"):
        # Call the parent constructor with default values or any provided ones
        super().__init__(name, health, attack, defence,type)

def checker(instance):
    if (instance,GrassMonster):
        print("This is a monster")
    else:
        print("This is not a monster")
Hello=GrassMonster()
Hello.printname()