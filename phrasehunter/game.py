# Create your Game class logic in here.
import random
from phrase import Phrase
import sys

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ["Hope you well",
                "Allah place you",
                "If there is a will you will", 
                "Treehouse TechDegree",
                "I need to No I have to"
                ]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        star_play = Phrase(self.active_phrase, self.guesses)
        print(star_play.display(), "\n")
        while True:
            self.get_guess()
            if "_" not in star_play.display():
                break
        if self.game_over():
            print(f"you solve it with {self.missed} tries ^_^ ")
    
    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        name = input("Could you please enter your name: ")
        print("---------------")
        print("* Hello {} *".format(name))
        print("---------------")

    def get_guess(self):
        disply_phrase = Phrase(self.active_phrase, self.guesses)
        missed = 5
        while True:
            guess = input("Please enter your letter guess: ")
            if guess.isalpha() and guess in self.active_phrase:
                self.guesses.append(guess)
                print(disply_phrase.display(),"\n")
                break
            elif guess not in self.active_phrase:
                print(f"You have {missed-1} out of {missed} lives remaining! \n")
                missed -= 1
                if missed == 0:
                    sys.exit("Sorry you out of lives, try agin!")
            else:    
                print("Please enter an alphabet letter\n")
            
        # if guess not in self.active_phrase:
        #     print(f"You have {missed-1} out of {missed} lives remaining! \n")
        #     missed -= 1
        #     if missed == 0:
        #         exit()


    def game_over(self):
        check_Win = Phrase(self.active_phrase, self.guesses)
        return check_Win.check_complete(check_Win.display())

gamee = Game()
gamee.start()
