# print('Week 3 Team activity, Dice game')
# import random
# number = random.randint(1,100)
# keep_playing = input('Do you want to keep playing (Yes or No)? ')
# print()
# while keep_playing.lower() == 'yes':
#     guess = int(input('What was your guess? '))
#     count = 0
#     while guess != number:
#         print()
#         print("That's not the number")
#         if guess > number:
#             print()
#             print('Lower')
#             print(f'That was guess number: {count + 1}.')
#         elif guess < number:
#             print()
#             print('Higher')
#             print(f'That was guess number: {count + 1}.')
#         guess = int(input('What was your guess? '))
#         count += 1
#         print()

#     else:
#         print()
#         print(f'You guessed it ({count + 1}) times and got it right!')
#         # import random
#         # number = random.randint(1,100)
#         keep_playing = input('Do you want to keep playing (Yes or No)? ')

# else:
#     print()
#     over = input('Game over. Press ENTER to exit.')

import random

class Card:
    
    def __init__(self):
        self.value = 0
        # self.value = int(input('Is your guess higher or lower? [1 - 13] '))
        self.points = 300
    
    def play(self):
        # card_guess = int(input('Is your guess higher or lower? [1 - 13] '))
        self.value = random.randint(1, 14)
       
        if self.value > self.points:
            # guess = True
            # if guess:
            self.points = 100 
        else:
            self.points = -75
