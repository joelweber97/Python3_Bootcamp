def statistics(original):
    with open(original,'r') as file:
        data = file.readlines()
    num_lines = len(data)
    num_words = sum([len(i.split(' ')) for i in data])
    num_characters = sum([len(x) for x in data])
    return {'lines': num_lines, 'words': num_words,'characters':num_characters}
    
    


#or even shorter we can use

def statistics(original):
    with open(original) as file:
        lines = file.readlines()
    
    return  {'lines': len(lines), 
            'words': sum(len(line.split(' ') for line in lines)), 
            'characters': sum((len(line) for line in lines))}


print(statistics('test.txt'))