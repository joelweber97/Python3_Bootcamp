'''
def find_factors(val):
	new_list = []
	potential = list(range(1, val+1))
	for i in potential:
		if val % i == 0:
			new_list.append(i)
	return new_list
			
print(find_factors(21))

'''

'''
def truncate(string, value):
    if value > 2:
        if value > len(string):
            return string
        else:
            return string[:value-3] + '...'
    else:
        return 'Truncation must be at least 3 characters.'
    
    
print(truncate('hel', 3))
'''
'''
def two_list_dictionary(ob1, ob2):
    while len(ob2) < len(ob1):
        ob2.append(None)
    return dict(zip(ob1, ob2))
    

print(two_list_dictionary(['a','b','c','d'], [1,2]))
'''


def range_in_list(lst, start = 0, end = None):
    if end is None:
        end = len(lst)
    return sum(lst[start:end+1])



print(range_in_list([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9], 1, 12))
print(range_in_list([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9], 1,100))
print(range_in_list([], 1, 12))
print(range_in_list([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9]))


















