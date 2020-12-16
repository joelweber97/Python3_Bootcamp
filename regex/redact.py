import re

text = 'Last night Mrs. Daisy and Mr. White murdered Ms. Chow'
#want to remove all the names

pattern = re.compile(r'(Mrs\.|Mr\.|Ms\.) [a-z]+', re.I)
result = pattern.sub('REDACTED', text)
print(result)
#Last night REDACTED and REDACTED murdered REDACTED


# we can use \g<1> to access the first capture group (Mrs.|Mr.|Ms.)
pattern = re.compile(r'(Mrs\.|Mr\.|Ms\.) [a-z]+', re.I)
result = pattern.sub('\g<1> REDACTED', text)
print(result)
#Last night Mrs. REDACTED and Mr. REDACTED murdered Ms. REDACTED


# We also put a capture group around the first letter of the last names
#We can use \g<2> to pull in that last name
pattern = re.compile(r'(Mrs\.|Mr\.|Ms\.) ([a-z])[a-z]+', re.I)
result = pattern.sub('\g<1> \g<2>', text)
print(result)
#Last night Mrs. D and Mr. W murdered Ms. C