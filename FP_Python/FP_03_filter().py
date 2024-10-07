# map, filter, zip, and reduce
#filter
# filter(function, data)
# runs the function on each item

my_list = [1, 2, 3]
def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)



