# allow us to generate a sequence of values over time

# e.g.: range() --> this is a generator

# allows us to use "yield".

# range(10) # creates one by one
# list(range(10)) # creates a list in memory

def make_list(num):
    result = []
    for i in range(num): # this is a generator, this does not create in memory
        result.append(i * 2)

    return result

my_list = make_list(10) # this list points to a location in memory
print(my_list) 