import pyfiglet
from colorama import init
from termcolor import colored
 
# use colorama to make termcolor work on Windows too
init()

possible_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

def ascii():
    if color in possible_colors:
        return colored(pyfiglet.figlet_format(text, font='slant'), color=color)
    else:
        return colored(pyfiglet.figlet_format(text, font='slant'), color='magenta')
        
        
text = input('what message do you want to print? ')
color = str(input('what color? ')).lower()
print(ascii())