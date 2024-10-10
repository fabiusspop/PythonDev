
def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print (err)
        #print(err)
        #print(f'Please enter numbers: {err}')
        # print('Please enter numbers.' + err)
        # print('Please enter numbers.')


# print(sum('1', 2))  # --> this gives a type error
# print(sum(1, 2))
print(sum(1, 0))
print(sum(1, '2'))