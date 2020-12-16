
def add(x,y):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    # the doctest above checks to see if the function returns 5 when 2 and 3 are used as arguments.
    # in this case we purposefully used multiplication instead of addition so the 
    # test will return false.
    return a * b
 
    

def double(values):
    """ double the values in a list
    >>> double([1,2,3,4])
    [2, 4, 6, 8]
    
    >>> double([])
    []
    
    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']
    
    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    #initially all 4 tests have failed.
    #an easy solution to fix one of the tests is to just return an empty list
    #return []
    #now only 3 test fail.
    
    #we change up the test to see if we can knock out any more of the failures
    return [2 * element for element in values]
    #now we have no failures.
    
    
    
def say_hi():
    """
    >>> say_hi()
    "hi"
    """
    #this will fail because doctests expects the string output to have single quotes ('hi') 
    

def true_that():
    """
    >>> true_that()
    True
    """
    return True
true_that()
#we get an error that says expected: True got: True..... there was a white space behind the doctest True so
#it threw an error.....

def make_dict(keys):
    """
    >>> make_dict(['a','b'])
    {'b': True, 'a': True}
    """
    return {key: True for key in keys}  
   #expected {'b': True, 'a': True} when it really got {'a': True, 'b': True} 
    #the order of the output matters so much.
    #in dicts the order doesnt matter, but in doctests it does.
    
