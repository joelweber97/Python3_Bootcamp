with open('haiku.txt', 'w') as file:
    file.write('writing files is great\n')
    file.write('heres another line of text\n')
    file.write('closing now, goodbye')
    
    
with open('haiku.txt', 'w') as file:
    file.write('not a haiku\n')
    file.write('overwriting the old haiku')
    
    
with open('lol.txt', 'w') as file:
    file.write('haha' * 1000)