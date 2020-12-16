from colorama import init
from termcolor import colored
 
# use colorama to make termcolor work on Windows too
init()
 
# then use termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_magenta'))



print(colored('hello world', color='yellow', on_color = 'on_green', attrs=['blink']))