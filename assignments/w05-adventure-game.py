from cmd import PROMPT
from unittest import case


game_state = True


class Player():
    locations = {
        'GO BACK': 'What would you like to do?',
        'origin': "You wake, finding yourself in a room with padded walls. You're clothed in a loose bodysuit with your arms strapped to your body with loose BELTS. Laying on a TABLE, with a chair nearby and a DOOR on the opposite wall. It feels as though the walls are closing in!",
        'BELTS': 'You inspect the belts that restrain you, they appear frayed, perhaps you could BREAK FREE? They are a cotton-like material with synthetic qualities, tied with a simple KNOT. The walls make an erie grating sound.',
        'TABLE': 'The table you find yourself on is a simple stainless steel construction, with DRAWERS along the side, and a pull out STOOL at one end. Trying to remember how you got here, the sound of the walls moving in snaps you back to reality.',
        'DOOR': 'You hobble over to the door, thin light peeks through around the EDGES. The door does not have a window, nor a handle you can see. Perhaps you can PUSH on it? Standing at the end of the room, it is more apparent that walls are indeed making the room more rectangular.',
        'BREAK FREE': 'Exerting all the force you can muster, you rip out of the binding enough to untie the rest. You gain a single belt, and place it in your pocket.',
        'KNOT': 'You attempt to untie yourself, but with what? Your hands are bound. Perhaps you can BREAK FREE? ',
        'DRAWERS': 'You open the drawers one at a time, finding a KNIFE, a SYRINGE filled with an unknown fluid, and a BOOK.',
        'KNIFE': 'You take the knife.',
        'SYRINGE': 'You inspect the syringe, cannot determine it\'s contents, and on strong impulse, you inject yourself. This was not wise, as darkness creeps into your vision, you hear the walls creep in.',
        'BOOK': 'You thumb through the book, finding nothing important and wasting precious time.',
        'STOOL': 'You inspect the stool, finding nothing interesting.',
        'EDGES': 'You inspect the edges. They appear wide enough for a small object to slide between, but too thin for your fingers. You can clearly see the latch keeping it shut.',
        'EDGES KNIFE': 'You slide the knife into the edge, unlatching the door!',
        'DOOR PUSH LOCKED': 'You push on the door, but it is firmly latched shut! If only you had something sharp to slide into them, you might be able to unlatch it.',
        'DOOR PUSH UNLOCKED': 'You push open the door, on the other side is a ledge with hooks of sorts lining the edge, perhaps supports for a broken railing? There is a drop of about 10 feet onto a glass walkway that leads to a windowed door, you can see outside. LOWER YOURSELF down with your belt or DROP DOWN?',
        'DROP DOWN': 'You drop down, shattering the glass walkway, and plummeting into complete darkness.',
        'LOWER YOURSELF BELT': 'You lower yourself down, gently falling the couple feet to the delicate glass walkway, and exit the building. You escape into the unknown, and unfamiliar landscape, alive. YOU WIN',
        'LOWER YOURSELF NO BELT': 'You attempt to lower yourself, wishing you had something to help lower yourself further. You slip and fall, crashing through the glass walkway',
        'PUSH': '',
        'LOWER YOURSELF': ''
    }
    prompts = {
        'origin': ['BELTS', 'TABLE', 'DOOR'],
        'BELTS': ['BREAK FREE', 'KNOT'],
        'TABLE': ['DRAWERS', 'STOOL'],
        'DOOR': ['EDGES', 'PUSH'],
        'BREAK FREE': ['GO BACK'],
        'KNOT': ['BREAK FREE'],
        'DRAWERS': ['KNIFE', 'SYRINGE', 'BOOK'],
        'KNIFE': ['GO BACK'],
        'SYRINGE': [],
        'BOOK': ['GO BACK'],
        'STOOL': ['GO BACK'],
        'EDGES': ['GO BACK'],
        'EDGES KNIFE': ['GO BACK'],
        'DOOR PUSH LOCKED': ['GO BACK'],
        'DOOR PUSH UNLOCKED': ['LOWER YOURSELF', 'DROP DOWN'],
        'LOWER YOURSELF': '',
        'LOWER YOURSELF BELT': '',
        'LOWER YOURSELF NO BELT': '',
        'GO BACK': ['BELTS', 'TABLE', 'DOOR'],
    }

    def __init__(self):
        print("New game!")
        self.location = 'origin'
        self.prompt = 'origin'
        self.belt = False
        self.knife = False
        self.door_locked = True
        self.distance_from_walls = 13
        self.player_crushed = False

    def move_walls_closer(self):
        self.distance_from_walls -= 1
        if self.distance_from_walls < 1:
            self.player_crushed = True
            return 'The walls have crushed you. You are dead.'
        else:
            return self.distance_from_walls


class Game():

    def __init__(self):
        self.player = Player()

    def give_scenario(self):
        print(self.player.locations[self.player.location])
        self.move_walls()
        prompt = input(
            self.player.prompts[self.player.location]).upper()
        return prompt

    def set_location(self, location):
        self.player.location = location

    def verify_location(self, location):
        for i, possible_location in enumerate(self.player.locations):
            if location == possible_location:
                return True
            if i == len(self.player.locations) - 1:
                if self.player.distance_from_walls != 10:
                    return False

    def incorrect_location(self):
        print("You can't do that here.")

    def move_location(self, location):
        if self.verify_location(location) == True:
            self.set_location(location)
        else:
            print("That is not an appropriate response, try again")

    def check_prompt(self, prompt):
        if prompt == 'BREAK FREE':
            self.player.belt = True
            self.set_location(prompt)
        elif prompt == 'KNIFE':
            if self.player.location == 'DRAWERS':
                self.player.knife = True
                self.set_location(prompt)
            else:
                self.incorrect_location()
        elif prompt == 'SYRINGE':
            print(self.player.locations['SYRINGE'])
            self.lose_game("You were crushed by the walls. You are dead.")
        elif prompt == 'EDGES':
            if self.player.knife == True:
                self.player.door_locked = False
                self.set_location('EDGES KNIFE')
        elif prompt == 'PUSH':
            if self.player.door_locked == True:
                self.set_location('DOOR PUSH LOCKED')
            else:
                self.set_location('DOOR PUSH UNLOCKED')
        elif prompt == 'DROP DOWN':
            if self.player.location == 'DOOR PUSHED UNLOCKED':
                print(
                    'You fall hard enough to shatter the walkway, plummeting into the darkness below')
                self.lose_game(
                    "You have fallen for an unknown time, perhaps infinitely. You are dead.")
            else:
                self.incorrect_location()
        elif prompt == 'LOWER YOURSELF':
            if self.player.location == 'DOOR PUSH UNLOCKED':
                if self.player.belt == True:
                    self.set_location('LOWER YOURSELF BELT')
                else:
                    print(self.player.locations['LOWER YOURSELF NO BELT'])
                    self.lose_game(
                        "You have fallen for an unknown time, perhaps infinitely. You are dead.")
            else:
                self.incorrect_location()
        else:
            self.set_location(prompt)

    def move_walls(self):
        if self.player.location != 'GO BACK':
            print('The walls move closer')
            player_info = self.player.move_walls_closer()
            if type(player_info) == str:
                self.lose_game(player_info)
            else:
                print(
                    f"You have {self.player.distance_from_walls} moves until the walls crush you.")

    def nudge_binding(self):
        print('You are bound. You go back.')
        self.player.location == 'start'

    def play_again(self):
        play_again = input('Would you like to play again? [y,n]').upper()
        if play_again == 'Y':
            del self.player
            self.player = Player()
        else:
            print("Thanks for playing!")
            exit()

    def win_game(self):
        print(f'You\'ve won the game! Congratulations!')
        self.play_again()

    def lose_game(self, cause_of_death):
        print(cause_of_death)
        self.play_again()

    def advance(self):
        print()
        prompt = self.give_scenario()
        if self.verify_location(prompt):
            self.check_prompt(prompt)
        else:
            print("Incorrect entry, was that a typo?")
            self.advance()
        if self.player.location == 'LOWER YOURSELF BELT':
            self.win_game()


game = Game()
while game.player.player_crushed == False:
    game.advance()
