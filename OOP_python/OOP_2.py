# Creating ur own obj

class PlayerCharacter:
    def __init__(self, name, age): # (dunder/magic method) constructor method
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('John', 21)
player2 = PlayerCharacter('Jane', 22)

print(player1)
print(player1.name)
print(player1.age)
print(player2.age)
print(player1.run())

print(player1) # player1 and player2 are at different memory loc
print(player2)

player2.attack = 50
print(player2.attack)

# help(player1) # shows blueprints
# help(list)

