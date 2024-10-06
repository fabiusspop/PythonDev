# __init__

# Creating ur own obj

class PlayerCharacter:

    membership = True       # class object attribute -> it s static

    def __init__(self, name='anonymous', age=1): # (dunder/magic method) constructor method
        if (age > 18):
            self.name = name # attributes
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')


# player1 = PlayerCharacter() # error --> no attribute provided
player1 = PlayerCharacter('Tom', 10)
print(player1.shout())



