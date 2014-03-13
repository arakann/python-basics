'''
Created on Mar 13, 2014

@author: ROO
'''

def fn():
    print 1

def add_test(fn):

listTests={'test1': 'passed', 'test2': 'fail', 'test3': 'fail', 'test4': 'notRun', 'test5': 'notRun', 'test6': 'notRun'}
def pending_tests(listTests):
    notRunLst = []
    [notRunLst.append(key) for key in listTests.keys() if listTests.get(key) == 'notRun']
    return notRunLst

print pending_tests(listTests)


def run(notRunLst):
    run = len(notRunLst)
    
    statusTuple = (run, passed, fail)
    return statusTuple 
    

def run_tests(listTests): 
    runTests = []
    [runTestsLst.append(key) for key in listTests.keys() if listTests.get(key) != 'notRun']
    return runTestsLst 

def passed_tests(listTests):
    passedTestsLst = []
    [passedTestsLst.append(key) for key in listTests.keys() if listTests.get(key) == 'passed']
    return passedTestsLst 

def failed_tests(listTests):
    failedTestsLst = []
    [failedTestsLst.append(key) for key in listTests.keys() if listTests.get(key) == 'fail'
    return failedTestsLst 

    
def clear_state():
    failedTestsLst = []
    passedTestsLst = []
    runTestsLst = []