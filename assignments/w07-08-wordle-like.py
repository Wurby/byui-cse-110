import random


class Game():
    WORDS = [
        "abandon",
        "bubbles",
        "cabbage",
        "dabbler",
        "fabrics",
        "gabbers",
        "habitat",
        "jackdaw",
        "karaoke",
        "lactase",
        "macabre",
        "napkins",
        "observe",
        "pacific",
        "painter",
        "quantum",
        "rabbits",
        "sabbath",
        "tabular",
        "tactics",
        "umpires",
        "vaccine",
        "waffler",
        "xanthin",
        "yardage",
        "zealous"
    ]

    def __init__(self):
        print("Welcome to Wordle-like! Guess the 7 letter word!")
        self.SECRET_WORD = random.choice(self.WORDS)
        self.GAME_TICK = 7
        self.HINT = "_ _ _ _ _ _ _"
        self.PLAY = True

    def take_input(self):
        print(f"You have {self.GAME_TICK} turns left.")
        guess = input("What is your guess? ").lower()
        self.GAME_TICK -= 1
        return guess

    def validate_guess(self, guess):
        print()
        if guess == self.SECRET_WORD:
            self.win_game(guess)

        if len(guess) != 7:
            print()
            print(
                f"Sorry, the guess must have the same number of letters as the secret word. Your word was {len(guess)} letters long.")
            print()
        else:
            self.modify_hint(guess)

        if self.GAME_TICK == 0:
            self.lose_game(guess)
        else:
            self.provide_hint()

    def provide_hint(self):
        print(f"Your hint is: {self.HINT}")

    def win_game(self, guess):
        print(f"Congratulations! {guess} was correct!")
        print(f"It took you {self.GAME_TICK} guesses!")
        exit()

    def lose_game(self, guess):
        print()
        print(f"{guess} was incorrect. You lost after {self.GAME_TICK} turns")
        exit()

    def modify_hint(self, guess):
        template = ["_", "_", "_", "_", "_", "_", "_"]
        for index, letter in enumerate(guess):
            if letter in self.SECRET_WORD:
                template[index] = letter.lower()
            if self.SECRET_WORD[index] == letter:
                template[index] = letter.upper()
        self.HINT = " ".join(template)

    def advance(self):
        guess = self.take_input()
        self.validate_guess(guess)


game = Game()
while game.PLAY:
    game.advance()
