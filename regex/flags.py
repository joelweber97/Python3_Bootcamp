# flags
# IGNORECASE/I 
# VERBOSE/X



import re
pat = re.compile(r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')


pat2 = re.compile(r"""
    ^([a-z0-9_\.-]+)        #first part of email
    @                       #single @ sign
    ([\da-z\.-]+)           #domain/email provided
    \.                      #a single .
    ([a-z\.]{2,6})$         #com/org/net/edu
""", re.VERBOSE)


match = pat2.search('thomas123@yahoo.com')
print(match.groups())
print(match.group())



pat3 = re.compile(r"""
    ^([a-z0-9_\.-]+)        #first part of email
    @                       #single @ sign
    ([\da-z\.-]+)           #domain/email provided
    \.                      #a single .
    ([a-z\.]{2,6})$         #com/org/net/edu
""", re.VERBOSE|re.IGNORECASE)
match2 = pat3.search('Thomas123@YAHOO.com')
print(match2.groups())
print(match2.group())