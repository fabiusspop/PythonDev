class User:
    def sign_in(self):
        print("Logged in.")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')
class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')

# When u do multiple inheritance, things can get complicated..
class HybridBorg(Wizard, Archer):   # multiple inheritance
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('John', 80, 100)
print(hb1.run())
print(hb1.check_arrows())
hb1.attack()
hb1.check_arrows()
hb1.sign_in() 