#can create a symbolic group name using ?P<string> in the regex
#and call the string in .group('string')


import re
def name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.group('first')) #prints tilda
    print(matches.group('last'))  #prints swinton
    

name('Mrs. Tilda Swinton')