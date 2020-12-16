
'''
import re

def parse_date(input):
    regex = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$')
    matches = regex.search(input)
    if matches:
        return {'d': matches.group(1), 'm': matches.group(2), 'y': matches.group(3)}
    return None
    

print(parse_date('11/11/2020'))
'''


import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.I)
    result = pattern.sub('CENSORED', input)
    return result
   
   
print(censor('frack off'))
