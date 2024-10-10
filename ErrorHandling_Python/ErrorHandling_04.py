
while True:
    try:
        age = int(input('What is your age? '))
        10 / age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break
    else:
        print('Thx.')
        # break
    finally:
        print("Ok, it's done")
    print("Can you hear me???")