# Set and Dictionaries Comprehension

my_list = {char for char in 'hello'} # we simply change the bracket notation into a set
my_list2 = {num for num in range(0, 10)}
my_list3 = [num * 2 for num in range(0, 10)]
my_list4 = {num for num in my_list2 if num % 2 == 0}

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# Dict comprehension
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value ** 2 for key, value in simple_dict.items()}
my_dict2 = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
# without a dictionary:
my_dict3 = {i: i * 2 for i in [1, 2, 3]}
 
print(my_dict)
print(my_dict2)
print(my_dict3)
