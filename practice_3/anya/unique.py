'''
Created on Mar 13, 2014

@author: ROO
'''


def unique(lst):
    Result = {i: None for i in lst}
    return Result.keys()

#print the result
'''print unique([1,2,3,4,1,1])'''


def testEmptyList(lst):
    try:
        assert lst != []
        return 'Pass'
    except AssertionError:
        raise AssertionError("Error:List is empty")

def testjustOneElement(lst):
    try:
        assert len(lst) > 1
    except AssertionError:
        raise AssertionError("Error:There is just one element in the list")

def testJust2EqualElem(lst):
    if len(lst) > 2:
        pass 
    elif len(lst) == 2 and lst[0] != lst[1]:
        pass
    else:
        raise AssertionError("Error:There are 2 equal elements in the list ") 


def testJust2UniqueElem(lst):
    if len(lst) > 2:
        pass
    elif len(lst) == 2 and lst[0] is lst[1]:
        pass
    else:
        raise AssertionError("Error:There are 2 unique elements in the list ")

testEmptyList([])
testjustOneElement([1])
testJust2EqualElem([1, 1])
testJust2UniqueElem([1, 2])