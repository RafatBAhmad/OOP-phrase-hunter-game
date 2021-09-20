import random
from phrasehunter.phrase import Phrase
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
        self.active_phrase = self.get_random_phrase().lower()
        star_play = Phrase(self.active_phrase, self.guesses)
        print(star_play.display(), "\n")
        while True:
            self.get_guess()
            if "_" not in star_play.display():
                break
        if self.game_over():
            print(f"you solve it with {len(self.guesses)} tries ^_^ ")
            self.new_game()

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        name = input("Could you please enter your name: ")
        print("---------------")
        print("* Hello {} *".format(name))
        print("---------------")

    def get_guess(self):
        disply_phrase = Phrase(self.active_phrase, self.guesses)

        while "_" in disply_phrase.display():
            guess = input("Please enter your letter guess: ").lower()
            if guess.isalpha() and len(guess) == 1:
                if guess in self.active_phrase:
                    self.guesses.append(guess)
                    print(disply_phrase.display(), "\n")
                else:
                    self.missed += 1
                    print(
                        f"You have {5-self.missed} out of 5 lives remaining! \n")
                    if self.missed == 5:
                        self.game_over()
                        self.new_game()
            else:
                print("\nPlease enter one alphabet letter\n ")

    def game_over(self):
        check_Win = Phrase(self.active_phrase, self.guesses)
        return check_Win.check_complete(check_Win.display())

    def new_game(self):
        play_again = input("Would you like to play again? [y]es/[n]o: ")
        if play_again.lower() == 'y':
            self.missed = 0
            self.active_phrase = None
            self.guesses = []
            self.start()
        else:
            sys.exit("see you agin ^ _ ^ ")


gamee = Game()
gamee.start()
