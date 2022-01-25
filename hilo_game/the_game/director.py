from the_game.hilo import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.is_playing = True
        self.score = 300
        self.total_score = 300

        for i in range(13):
            cards = Card()
            self.card.append(cards)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            # self.compare()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play_card = input("Play on? [y/n] ")
        self.is_playing = (play_card == "y")

    # def compare(self):
    #     card_guess = input('Is your guess higher or lower? [1 - 13] ')

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        # for i in range(len(self.card)):
        #     cards = self.card[i]
        #     cards.play()
        #     self.score += cards.points 
        # self.total_score += self.score

        cards = int(input('Is your guess higher or lower? [1 - 13] '))
        # cards.play()
        # self.score += cards.points 
        # self.total_score += self.score
        self.total_score += cards


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""

        for i in range(len(self.card)):
            cards = self.card[i]
            values += f"{cards.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
       