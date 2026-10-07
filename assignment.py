# Ellie Khoo
# AM
# Number Guessing Game

# imported module to generate random numbers
import random

# random number is generated and stored in variable
random_number = random.randint(1,10)

# created list to keep track of guesses
previous_guesses = []

# introduce user to game
print("Welcome to the Number Guessing Game!")
print("You'll have to guess a number between 1-10 to win.")
print("Good luck!")

# condition to keep running while loop until correct answer is guessed
correct_answer_picked = False

while correct_answer_picked == False:

    # asks user to enter their guess and gets their input as an integer
    user_guess = int(input("Enter a number between 1-10: "))

    # use loop to validate whether user's guess is in the range
    while user_guess < 1 or user_guess > 10:
        print("Invalid input!")
        user_guess = int(input("Enter a number between 1-10: "))

    # create boolean to check if user's guess passes requirements
    is_duplicate = False
    pass_requirements = False

    # uses loop to check for invalid guesses, asks to guess again if so
    while pass_requirements == False and previous_guesses != []:

        # uses loop to check for in range guess
        while user_guess < 1 or user_guess > 10:
            print("Invalid input!")
            user_guess = int(input("Enter a number between 1-10: "))

        # uses loop to check for duplicate guess
        is_duplicate = False
        for i in previous_guesses:
            if i == user_guess:
                print("You already guessed", i)
                print("Choose a different number.")
                print("Previous guesses:", previous_guesses)
                is_duplicate = True

        # uses if to check if requirements were passed, otherwise asks again and validates user's guess again
        if is_duplicate == True:
            user_guess = int(input("Enter a number between 1-10: "))
        else:
            pass_requirements = True

    # add guesses into list to check for duplicates
    previous_guesses.append(user_guess)
    print(previous_guesses)

    # evaluate whether user guessed the random number or if its higher or lower
    if user_guess > random_number:
        print("Try again! The random number is lower!")
        print("Previous guesses:", previous_guesses)
    elif user_guess < random_number:
        print("Try again! The random number is higher!")
        print("Previous guesses:", previous_guesses)
    else:
        print("Congratulations, you guessed correctly!")
        correct_answer_picked = True


