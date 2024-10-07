# list / set / dictionary comprehensions

# Instead of doing: ------------------------
# my_list = []
#
# for char in 'hello':
#     my_list.append(char)
#
# print(my_list)
# --------------------------------------------
# DO THIS: ----> [param for param in iterable]

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 10)]
my_list3 = [num * 2 for num in range(0, 10)]
my_list4 = [num for num in my_list2 if num % 2 == 0]
my_list5 = [num for num in range(0, 50) if num % 2 == 0]


print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)