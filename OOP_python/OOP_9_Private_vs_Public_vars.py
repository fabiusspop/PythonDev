# 2. Abstraction

# private?
# in python there s no true privacy
# "_" stands for a private variable
class PlayerCharacter:
    def __init__(self, name, age): #__init__ is a dunder method
        # we never write dunder methods (they have special meaning in python)
        self._name = name   # _ means this should be a private variable
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and i am {self._age} years old')

player1 = PlayerCharacter('John', 22)

# player1.name = "!!!"
# player1.speak = "BOOO"

print(player1.speak)
