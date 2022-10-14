game_state = True
class Player():
    def __init__(self):
        print("New game!")
        self.position = 'a'
        self.selection = ''
        self.status_effects = {'bound': True}
        self.belt = False
        self.knife = False
        self.player_crushed = False
        self.distance_from_wall = 10

    def fall_death(self):
        print('You have fallen to your death. You are dead.')

    def move_walls_closer(self):
        self.distance_from_wall -= 1
        if self.distance_from_wall == 0:
            self.player_crushed = True
            return 'The walls have crushed you. You are dead.'
        else:
            return self.distance_from_wall

    def set_selection(self, prompt):
        selection = input(prompt.upper())
    
    def display_inventory(self):
        print(self.inventory)

class Game():
    scenarios = {
        'start': 'What would you like to do?',
        'origin': "You wake, finding yourself in a room with padded walls. You're clothed in a loose bodysuit with your arms strapped to your body with loose BELTS. Laying on a TABLE, with a chair nearby and a DOOR on the opposite wall. It feels as though the falls are closing in!",
        'BELTS': 'You inspect the belts that restrain you, they appear frayed, perhaps you could BREAK FREE? They are a cotton-like material with synthetic qualities, tied with a simple KNOT. The walls make an erie grating sound.',
        'TABLE': 'The table you find yourself on is a simple stainless steel construction, with DRAWERS along the side, and a pull out STOOL at one end. Trying to remember how you got here, the sound of the walls moving in snaps you back to reality.',
        'DOOR': 'You hobble over to the door, thin light peeks through around the EDGES. The door does not have a window, nor a handle you can see. Perhaps you can PUSH on it? Standing at the end of the room, it is more apparent that walls are indeed making the room more rectangular.',
        'BREAK FREE': 'Exerting all the force you can muster, you rip out of the binding enough to untie the rest. You gain a single belt, and place it in your pocket.',
        'KNOT': 'You attempt to untie yourself, but with what? Your hands are bound. Perhaps you can BREAK FREE? ',
        'DRAWERS': 'You open the drawers one at a time, finding a KNIFE, a SYRINGE filled with an unknown fluid, and a BOOK.',
        'KNIFE': '',
        'SYRINGE': '',
        'BOOK': '',
        'STOOL': 'You inspect the stool, finding nothing interesting.',
        'EDGES1': 'You inspect the edges. They appear wide enough for a small oject to slide between, but too thin for your fingers. You can clearly see the latch keeping it shut.',
        'ESGES2': 'You slide the knife into the edge, unlatching the door!',
        'DOOR1': 'You push on the door, but it is firmly latched shut! If only you had something sharp to slide into them, you might be able to unlatch it.',
        'DOOR2': 'You push open the door, on the other side is a ledge with hooks of sorts lining the edge, perhaps supports for a broken railing? There is a drop of about 10 feet onto a glass walkway that leads to a windowed door, you can see outside. LOWER YOURSELF down with your belt or DROP DOWN?',
        'DROP DOWN': 'You drop down, shattering the glass walkway, and plumeting into complete darkness.',
        'LOWER YOURSELF': 'You lower yourself down, gently falling the couple feet to the delicate glass walkway, and exit the building. You escape into the unknown, and unfamiliar landscape, alive. YOU WIN'
        }
    prompts = {
        'start': ['BELTS', 'TABLE', 'DOOR'],
        'origin': ['BELTS', 'TABLE', 'DOOR'],
        'BELTS': ['BREAK FREE', 'KNOT'],
        'TABLE': ['DRAWERS', 'STOOL'],
        'DOOR': ['EDGES', 'PUSH'],
        'BREAK FREE': ['GO BACK'],
        'KNOT': ['BREAK FREE'],
        'DRAWERS': ['KNIFE', 'SYRINGE', 'BOOK'],
        'KNIFE': ['GO BACK'],
        'BOOK': ['GO BACK'],
        'STOOL': ['GO BACK'],
        'EDGES1': ['GO BACK'],
        'EDGES2': ['GO BACK'],
        'DOOR1': ['GO BACK'],
        'DOOR2:': ['LOWER YOURSELF', 'DROP DOWN'],
    }
    def __init__(self):
        self.player = Player()
        self.player_location = 'origin'
        self.door_open = False
    
    def give_prompt(self, player_location):
        prompt_response = input(self.scenarios[player_location], self.prompts[player_location]).upper()
        if prompt_response == 'GO BACK':
            self.player_location = "START"
        if prompt_response == 'KNOT':
            if self.player.belt == True:
                print("You've already broken free.")
                self.player_location = 'start'
                prompt_response = input(self.scenarios[player_location], self.prompts[player_location]).upper()
        if prompt_response == 'BELTS':
            self.player.belt = True
        if prompt_response == "SYRINGE":
            print("You inspect the syringe, and on a whim inject yourself with it. It was not a wise choice. You feel darkness immediately creeping into the edges of your vision. As you fall asleep, mind fuzzing, you recognize the walls still moving in.")
            self.lose_game("You foolishly injected yourself with what appears to be a sleep inducing medication. You are inevitably crushed by the walls. You are dead.")
        if prompt_response == 'KNIFE':
            self.player.knife = True
        if prompt_response == 'EDGES':
            if self.player.knife == True:
                prompt_response = 'EDGES2'
            else:
                prompt_response = 'EDGES1'
        if prompt_response == 'DOOR':
            if self.player.belt == False:
                prompt_response = 'DOOR1'
            else:
                prompt_response = 'DOOR2'
        if prompt_response == 'DROP DOWN':
            if self.door_open == True:
                self.lose_game(self.player.fall_death)
        if prompt_response == 'LOWER YOURSELF':
            if self.player.belt == False:
                print("With what?")
                self.nudge_binding()
                self.win_game()

        self.move_walls()
        self.player_location = prompt_response

    def move_walls(self):
        print('The walls move closer')
        player_info = self.player.move_walls_closer()
        if type(player_info) == 'str':
            self.lose_game(player_info)

    def nudge_binding(self):
        print('You are bound. You go back.')
        self.player_location == 'start'
        
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
        


game = Game()

while game:
    game.give_prompt()