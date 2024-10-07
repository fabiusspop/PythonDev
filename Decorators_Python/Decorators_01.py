# @classmethod
# @staticmethod

def hello(func):
    func()

def greet():
    print("still here!")

# greet = hello
# del hello
# hello()
# print(greet()) # still pointing in memory to the "hello()" location

a = hello(greet)
print(a)
# ability of functions to act as variables