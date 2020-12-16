#https?://www\.[A-Za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//]*
#http with an optional s, :, //, www, ., 2 to 256 letters or dashes, ., 2 to 6 lower case letters, and 0 or more of any letter number @ : % _ \ + . ~ & //
#http://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/2354253#question



import re
url_regex = re.compile(r'https?://www\.[A-Za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//]*')
match = url_regex.search('http://www.youtube.com/videos')
print(match.group())  #prints the url


# lets see how parans change things
# lets say we have a bunch of users submitting urls
# we want to do analytics on them.
# maybe see how mnay sites come from youtube.com or 
# how many sites are http vs https
#we add parens before the www. and after the .com
url_regex1 = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//]*)')
match1 = url_regex1.search('http://www.youtube.com/videos')
print(match1.group())  #prints the url that matches  'http://www.youtube.com/videos'
print(match1.group(0))  #prints the url that matches  'http://www.youtube.com/videos'
print(f"protocol: {match1.group(1)}")  #prints the first match that is contained in the parens   'http'
print(f"domain: {match1.group(2)}")  #prints the second match that is contained in the parens   'www.youtube.com'
print(f"everything else: {match1.group(3)}")  #prints the third match that is contained in the parens   '/videos'
print(match1.groups())  #prints a tuple of strings that match based on where the parens are   ('http', 'www.youtube.com', '/videos')

