import colorama
from colorama import Fore
colorama.init()

colors = {
    "BLACK": Fore.BLACK,
    "RED": Fore.RED,
    "PINK": Fore.LIGHTRED_EX,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW,
    "BLUE": Fore.BLUE,
    "MAGENTA": Fore.MAGENTA,
    "CYAN": Fore.CYAN,
    "WHITE": Fore.WHITE

}

print("What is your favorite color? (Try blue for fun)")
favorite_color = input().upper()
statement = "your favorite color is:"
if favorite_color in colors.keys():
    print(statement, colors[favorite_color], favorite_color)
else:
    print(Fore.LIGHTBLACK_EX, statement, favorite_color)
