# a function should not produce side effects
# keeping code clean and avoiding bugs

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list  
    # return print(new_list)  # this would have side effects! (print)

print(multiply_by2([1, 2, 3])) # is this a pure function???
# 1. always return the same output
# 2. does it produce side effects? No!
