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
print("You'll have 5 tries to guess a number between 1-10 to win.")
print("Good luck!")
print()

# condition to keep running while loop until correct answer is guessed
correct_answer_picked = False

# variable to keep track of number of tries
tries = 5

# loop 
while correct_answer_picked == False and tries > 0:

    # count user's tries
    tries -= 1

    # asks user to enter their guess and gets their input as an integer
    user_guess = int(input("Enter a number between 1-10: "))

    # use loop to validate whether user's guess is in the range
    while user_guess < 1 or user_guess > 10:
        print("Invalid input!")
        print()
        user_guess = int(input("Enter a number between 1-10: "))

    # create boolean to check if user's guess passes requirements
    is_duplicate = False
    pass_requirements = False

    # uses loop to check for invalid guesses, asks to guess again if so and checks if new guess is valid again
    while pass_requirements == False and previous_guesses != []:

        # uses loop to check for in range guess
        while user_guess < 1 or user_guess > 10:
            print("Invalid input!")
            print()
            user_guess = int(input("Enter a number between 1-10: "))

        # uses loop to check for duplicate guess
        is_duplicate = False
        for i in previous_guesses:
            if i == user_guess:
                print("You already guessed", i)
                print("Choose a different number.")
                print("Previous guesses:", previous_guesses)
                print()
                is_duplicate = True

        # uses if to check if requirements were passed, otherwise asks again and validates user's guess again
        if is_duplicate == True:
            user_guess = int(input("Enter a number between 1-10: "))
        else:
            pass_requirements = True

    # add guesses into list to check for duplicates
    previous_guesses.append(user_guess)

    # evaluate whether user guessed the random number or if its higher or lower plus closing statements
    if tries < 1:
        print("You ran out of tries!")
        print()
        print("Your guesses were:", previous_guesses)
        print("The correct number:", random_number)
        print("Game over!")
    elif user_guess > random_number:
        print("Try again! The random number is lower!")
        print("Previous guesses:", previous_guesses)
        print()
    elif user_guess < random_number:
        print("Try again! The random number is higher!")
        print("Previous guesses:", previous_guesses)
        print()
    else:
        print("Congratulations, you guessed correctly!")
        print("See you next time!")
        correct_answer_picked = True

    # tell users how many tries they have left
    if tries == 0:
        print()
    elif tries == 1 and correct_answer_picked != True:
        print("You have", tries, "try left!")
        print()
    elif tries < 5 and correct_answer_picked != True:
        print("You have", tries, "tries left!")
        print()



