from the_game.hilo import Card

import random
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[card]): A list of the card instance.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        else:
            print('Game Over!')

    def get_inputs(self):
        """Ask the user if they want to play.

        Args:
            self (Director): An instance of Director.
        """
        play_card = input("Play on? [y/n] ")
        self.is_playing = (play_card == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        number = random.randint(1, 13) # Generate a random card number from 1 to 13
        cards = int(input('Guess, is the next card higher or lower? [1 - 13] ')) # Player guesses the next card
        print(f'The card is: {number}!')
        if cards > number:
            print('You guessed higher, your score is now 100 points more')
            cards = 100
        else:
            print('You guessed lower, your score is now 75 points less')
            cards = -75
      
        self.total_score += cards

        # Terminate the game when score is zero
        if self.total_score == 0:
            self.is_playing = False
            return
            
    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to play again if they their score is > zero. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"Total score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
       