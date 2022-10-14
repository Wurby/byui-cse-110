game_state = True


class Game():
    scenarios = {
        'a': "You wake, finding yourself in a room with padded walls. You're clothed in a loose bodysuit with your arms strapped to your body with loose BELTS. Laying on a TABLE, with a chair nearby and a DOOR on the opposite wall.",
        'a1': 'You inspect the belts that restrain you, they appear frayed, perhaps you could BREAK FREE? They are a cotton-like material with synthetic qualities, tied with a simple KNOT.',
        'a2': 'The table you find yourself on is a simple stainless steel construction, with DRAWERS along the side, and a pull out STOOL at one end.',
        'a3': 'You hobble over to the door, thin light peeks through around the EDGES. The door does not have a window, nor a handle you can see. Perhaps you can PUSH on it?',
        'b': '',
        'ba': '',
        'bb': '',
        'bc': '',
        'c': '',
        'ca': '',
        'cb': '',
        'cc': ''}
    prompts = {
        '1': ['BELTS', 'TABLE', 'DOOR'],
        '1a': ['BREAK FREE', 'KNOT'],
        '1b': ['DRAWERS', 'STOOL'],
        '1c': ['EDGES', 'PUSH'],

    }

    def __init__(self):
        self.position = 'a'
        self.answer = ''
        self.play = True

    def set_answer(self, question):
        self.answer = input(question)

    def set_position(self, position):
        self.position = position

    def present_scenario(self):
        print(self.scenarios[self.position])

    def present_prompt(self):
        self.position
