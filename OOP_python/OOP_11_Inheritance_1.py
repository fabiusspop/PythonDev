# 3 - Inheritance

class User:
    def sign_in(self):
        print("Logged in.")

class Wizard(User):     # the parent class from which wizard inherits from
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}' )


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')



wizard1 = Wizard('Merlin', 80)
archer1 = Archer('Robin', 120)

# isinstance(instance, Class))
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

# everything in pyhton inherits from the base object class python comes with
print(isinstance(wizard1, object))