import re
titles = ['Significant Others (1987)',
    'Tales of the City (1978)',
    'The days of Anna Madrigal (2014)',
    'Mary Ann in Autmn (2010)',
    'Further Tales of the City (1982)',
    'Babycakes (1894)',
    'More Tales of the City (1980)',
    'Sure of you (1989)',
    'Michael Tolliver Lives (2007)']
    
fixed_titles = []
pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
for book in titles:
    result = pattern.sub('\g<2> - \g<1>', book)
    fixed_titles.append(result)

fixed_titles.sort()
print(fixed_titles)
