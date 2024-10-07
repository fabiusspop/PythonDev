# map, filter, zip, and reduce

# map
# map(function, [1, 2, 3])

my_list = [1, 2, 3]
def multiply_by2(item):
    return item * 2

# print(multiply_by2([1, 2, 3]))

print(map(multiply_by2, [1, 2, 3]))
print(list(map(multiply_by2, [1, 2, 3])))
print(list(map(multiply_by2, my_list))) # returns a new list without side effects
print(my_list) # pure function --> doesn't affect the outside world



