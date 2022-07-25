import random

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Class
class Hangman:

    #  Constructor Method
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

        # Guess the letter method
        def guess(self, letter):
            if letter in self.word and letter not in self.guessed_letters:
                self.guessed_letters.append(letter)
            elif letter not in self.word and letter not in self.missed_letters:
                self.missed_letters.append(letter)
            else:
                return False
            return True

        def hangman_over(self):
            return self.hangman_won() or (len(self.missed_letters) == 6)

        def hangman_won(self):
            if '_' not in self.hide_word():
                return True
            return False

        def hide_word(self):
            rtn = ''
            for letter in self.word:
                if letter not in self.guessed_letters:
                    rtn += '_'
                else:
                    rtn += letter
            return rtn

        def print_game_status(self):
            print(board[len(self.missed_letters)])
            print('\nWords: ' + self.hide_word())
            print('\nWrong Letters: ', )
            for letter in self.missed_letters:
                print(letter, )
            print()
            print('Right letters : ', )
            for letter in self.guessed_letters:
                print(letter, )
            print()

