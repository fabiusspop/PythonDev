# @classmethod and @staticmethod

# __init__

# Creating ur own obj

class PlayerCharacter:

    membership = True       # class object attribute -> it s static

    def __init__(self, name, age): # (dunder/magic method) constructor method
        self.name = name  # attributes
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    # decorator
    @classmethod
    def adding_things(cls, num1, num2): # cls --> class PlayerCharacter
        return cls('JANE', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2): # we use if we don t care about the attributes or class states
        return num1 + num2  


#player1 = PlayerCharacter('John', 20)

#print(player1.adding_things(2, 3))

#print(PlayerCharacter.adding_things(2, 3))

player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)


