print('=' * 40)
print('Welcome to Hangman game')
print('''Choose the language you want to play:
[1] English
[2] Português
[3] Español''')
print('=' * 40)

option = int(input('Enter your language:'))

if option == 2:
    from hangman_Port import *

if option == 1:
    from hangman_Eng import *
