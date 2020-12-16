def make_song(verses = 99, beverage = 'soda'):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)
        
            
beer_song = make_song(5, 'beer')
print(next(beer_song))
print(next(beer_song))
print(next(beer_song))
print(next(beer_song))
print(next(beer_song))
print(next(beer_song))
print(next(beer_song))
print(next(beer_song))