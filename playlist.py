

playlist = {
    'title': 'Patagonia Bus',
    'Author': 'Colt Steele',
    'songs':[
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.50},
        {'title': 'song2', 'artist': ['kitty', 'dj cat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}  

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)