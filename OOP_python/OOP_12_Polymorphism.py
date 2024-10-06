# 4 - Polymorphism
# poly = many
# morphism = forms

class User:
    def sign_in(self):
        print("Logged in.")

    def attack(self):
        print("do nothing")

class Wizard(User):     # the parent class from which wizard inherits from
    def __init__(self, name, power):
        self.name = name
        self.power = power
    #override the attack method
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}' )


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

def player_attack(char):
    char.attack()

wizard1 = Wizard('Merlin', 80)
archer1 = Archer('Robin', 120)

# player_attack(wizard1)
# player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()

wizard1.attack()