def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(text) is not str:
        raise TypeError('Text must be a string')
    if color not in colors:
        raise ValueError('Not a valid color')
colorize('hello', 'red')

