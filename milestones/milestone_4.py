import random

class Hangman:
    ''' Doc Strings etc... '''

    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        

    def _check_guess(self, guess):

        guess = guess.lower()

        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            print(self.word_guessed)        
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left')

    def ask_for_input(self):

        guess = input('Enter a single letter: ')
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self._check_guess(guess)
            self.list_of_guesses.append(guess)

