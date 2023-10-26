import random

def check_guess(guess):
    guess = guess.lower()
    
    if guess in fruit:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


def ask_for_input():
    
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)

fruit_list = ['kiwi', 'strawberry', 'mango', 'banana', 'apple']
fruit = random.choice(fruit_list)


ask_for_input()