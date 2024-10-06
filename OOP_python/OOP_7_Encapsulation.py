# 4 pillars of OOP:

# 1. Encapsulation -> binding of data and functions into attributes and methods

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter('John', 22)
player1.speak()

'hellooo'.capitalize() # e.g. of functionalities encapsulated to use

player2 = {'name': 'jane', 'age': 23}
print(player2['name']) 