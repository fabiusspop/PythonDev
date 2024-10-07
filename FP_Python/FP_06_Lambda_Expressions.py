# Lambda expressions
# - one time anonymous functions
# useful for functions that:
# a) you use only once
# we do not need to store it in our machines
from functools import reduce

# lambda param: action(param)

my_list = [1, 2, 3]

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(map(multiply_by2, my_list)))
print(list(map(lambda item: item * 2, my_list)))
print()

print(list(filter(only_odd, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print()

print(reduce(accumulator, my_list, 0))
print(reduce(lambda acc, item: acc + item, my_list))






