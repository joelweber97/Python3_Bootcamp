import re

def extract_phone(input):
    #create the regex object
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    #search the regex object and save it to a variable as a re.Match object
    match = phone_regex.search(input)
    #need to test if match is a valid regex object before we can call .match() on it
    #this is done by the if match is True: group() it. Otherwise just return None instead.
    if match:
        return match.group()
    else:
        return None
    
print(extract_phone('my number is 715 305-4372'))   #715 305-4372
print(extract_phone('my number is 715 305-437222'))  #None

def extract_all_phone(input):
    #create the regex object
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    #don't need the if statement like above because .findall() 
    #returns a list of strings not a Match object
    #if no phone numbers in the string it will return an empty list
    return phone_regex.findall(input)

print(extract_all_phone('my numger is 715 305-2345 or 123 123-1234'))  #['715 305-4372', '123 123-1234']
print(extract_all_phone('my numger is 7152-2345 or 23-1234'))  #[]
 
 
 #a lot of regex is just validating input
 
def is_valid_phone(input):
    #create the regex object  Has to start and end with the values in the phone number
    # no other characters are permitted.
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    #search the regex object and save it to a variable as a re.Match object
    match = phone_regex.search(input)
    #need to test if match is a valid regex object before we can call .match() on it
    #this is done by the if match is True: group() it. Otherwise just return None instead.
    if match:
        return True
    else:
        return False
    
print(is_valid_phone('715 333-3333'))   #True
print(is_valid_phone('a 715 333-3333 d')) #False
print(is_valid_phone('715 333-3333 asdf'))  #False    
    

def is_valid_phone2(input):
    #create the regex object with the same regex from 2 above (no ^ or $)
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    #search the regex object for a fullmatch and save it to a variable as a re.Match object
    match = phone_regex.fullmatch(input)
    #need to test if match is a valid regex object before we can call .match() on it
    #this is done by the if match is True: group() it. Otherwise just return None instead.
    if match:
        return True
    else:
        return False


print(is_valid_phone2('715 333-3333'))   #True
print(is_valid_phone2('a 715 333-3333 d')) #False
print(is_valid_phone2('715 333-3333 asdf'))  #False







