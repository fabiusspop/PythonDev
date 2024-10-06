# 2. Abstraction
# abstracting information user does not need to see/know

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and i am {self.age} years old')

player1 = PlayerCharacter('John', 22)

player1.speak()
print((1, 2, 3, 1).count(1))
print(len((1, 2, 3, 1)))

# camera.takePicture()
player1.name = "!!!"
player1.speak = "BOOO"

print(player1.speak) # isn t this bad?
