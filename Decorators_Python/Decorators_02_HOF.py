# Higher Order Functions

def greet(func): # function that accepts inside its params another function
    func()

def greet2():
    def func():
        return 5
    return func # higher order function

# map(), reduce(), filter() --> Higher order functions


