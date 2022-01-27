# import random
class Card:
    
    def __init__(self):
        self.value = 0
        self.points = 300
        self.guess = 0
    
    # TO THIS POINT THE GAME IS WORKING, NOT SURE WHAT TO DO WITH THE BELOW CODE OR IT'S NOT NEEDED.

    # def play(self):
    #     self.guess = int(input('Is your guess higher or lower? [1 - 13] '))
    #     self.value = random.randint(1, 14)


    #     print(f'The card is: {self.guess}!') ##
       
    #     if self.guess > self.value:
    #         # guess = True
    #         # if guess:
    #         print('You guessed higher, your score is now 100 points more') ##
    #         self.points += 100 
    #     else:
    #         print('You guessed lower, your score is now 75 points less')
    #         self.points -= 75

    #     # self.total_score > 0