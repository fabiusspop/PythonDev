# Creating ur own obj

class PlayerCharacter:

    membership = True       # class object attribute -> it s static

    def __init__(self, name, age): # (dunder/magic method) constructor method
        if (PlayerCharacter.membership): # or self.membership
            self.name = name # attributes
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('John', 21)
player2 = PlayerCharacter('Jane', 22)

print(player1.name)
print(player2.membership) # actual attribute of the class, not dynamic

print(player1.shout())

print(player1.run('helloooo'))




