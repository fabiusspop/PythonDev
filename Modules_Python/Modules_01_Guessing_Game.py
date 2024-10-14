from random import randint

answer = randint(1, 10)

while True:
    try:
        user_guess = int(input("Guess the number (1-10) --> "))

        if 0 < user_guess < 11:
            if (int(user_guess) == answer):
                print("Correct guess! ^.^ ")
                break
        else:
            print("The number must be between [1, 10]!")

    except ValueError:
        print("Enter a number. (1-10)")
        continue