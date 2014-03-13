'''
Created on Mar 13, 2014

@author: ROO
'''

def assert_equal(a, b, message="Error:a is not equal to b"): 
    if a==b: 
        return True 
    else: 
        raise AssertionError(message) 


def assert_not_equal(a, b, message= "Error: a is  equal to b"): 
    if a != b: 
        return True 
    else: 
        raise AssertionError(message) 


def assert_true(a,message="Error:a is not True"): 
    try: 
       assert a 
    except AssertionError: 
       raise AssertionError(message) 
    

def assert_false(a,message="Error:a is not False"): 
    try: 
       assert bool(a) == False 
    except AssertionError: 
       raise AssertionError(message) 
    
def assert_is(a,b,message="Error:a is not b"): 
    try: 
       assert a is b 
    except AssertionError: 
       raise AssertionError(message) 
    
def assert_is_not(a,b,message="Error:a is b"): 
    try: 
       assert a is not b 
    except AssertionError: 
       raise AssertionError(message) 
    
def assert_is_none(a,message="Error:a is not None"): 
    try: 
       assert a is None 
    except AssertionError: 
       raise AssertionError(message) 

def assert_is_not_none(a,message="Error:a is None"): 
    try: 
       assert a is not None 
    except AssertionError: 
       raise AssertionError(message) 
    
def assert_in(a,b,message="Error:a is not in b"): 
    try: 
       assert a in b 
    except AssertionError: 
       raise AssertionError(message) 
    
def assert_not_in(a,b,message="Error:a is  in b"): 
    try: 
       assert a not in b 
    except AssertionError: 
       raise AssertionError(message) 
  
assert_not_in(1, [1,3,4], "Not default Exception message")


