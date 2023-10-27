import random

# Task 1
fruit_list = ['kiwi', 'strawberry', 'mango', 'banana', 'apple']

# Task 2
guess_fruit = random.choice(fruit_list)

# Task 3
letter_guess = input('Enter a single letter: ')

# Task 4
if len(letter_guess) == 1 and letter_guess.isalpha() == True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')

