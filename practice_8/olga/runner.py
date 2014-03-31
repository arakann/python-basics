import traceback
from assertions import *
from examples_5.todo_tests import *
import functools
from datetime import datetime
import sys
import os



def logger(f):
    def run_wrapper(*args, **kwargs):
        log_dir = "C:\\test-results\[{isodatetime}]-tests-results.txt".format(isodatetime=datetime.now().isoformat().replace(':', '.'))
        if not os.path.exists(os.path.dirname(log_dir)):
            os.makedirs(os.path.dirname(log_dir))
        std = sys.stdout
        sys.stdout = open(log_dir, 'w')
        with  sys.stdout:
            f(*args, **kwargs)
        sys.stdout = std
    return run_wrapper

class TestRunnerReporter(object):
    tests = {}
    PENDING = "pending"
    FAILED = "failed"
    PASSED = "passed"
    reporter = None
    
    def set_up(self): pass
    def tear_down(self): pass
    
    def __init__(self, some_reporter):
        self.reporter = some_reporter
        test_case = TodoTestCase()
        #self.tests = {m: [self.PENDING, getattr(test_case, m)] for m in dir(test_case) if m.startswith("test_")}
        if hasattr(test_case, "set_up"):
            self.set_up = getattr(test_case, "set_up")
        if hasattr(test_case, "tear_down"):
            self.tear_down = getattr(test_case, "tear_down")
        self._passed_tests = []
        self._ran_tests = []
        self._pending_tests = []
        self._failed_tests = []
        #self._pending_tests =  [getattr(test_case, m) for m in dir(test_case) if m.startswith("test_")]
    
    def add_test(self, fn):
        self.tests[fn.__name__] = ["pending", fn]
        
    #@logger
    def run(self):
        for x in self.tests:
            if self.tests[x][0] == "pending":
                self.reporter.report_test_started(x)
                try:
                    test = self.tests[x][1]
                    test()
                    self.tests[x] = ["passed", test]
                    self.reporter.report_test_finished(x)
                except Exception:
                    self.tests[x] = ["failed", test]
                    self.reporter.report_test_finished(x, traceback.format_exc())
        self.ran_tests = [x for x in self.tests if (self.tests[x][0] == "passed" or self.tests[x][0] == "failed")]
        self.passed_tests =  [x for x in self.tests if self.tests[x][0] == "passed"]
        self.failed_tests = [x for x in self.tests if self.tests[x][0] == "failed"]
        self.pending_tests = [x for x in self.tests if self.tests[x][0] == "pending"]
        self.reporter.report_all_finished(self.passed_tests, self.failed_tests, self.ran_tests)

    @property
    def ran_tests(self):
        return self._ran_tests
    
    @ran_tests.setter
    def ran_tests(self, tests_list):
        self._ran_tests = tests_list
    
    
    @property
    def passed_tests(self):
        return self._passed_tests
    
    @passed_tests.setter
    def passed_tests(self, tests_list):
        self._passed_tests = tests_list
    
    @property
    def failed_tests(self):
        return self._failed_tests
    
    @failed_tests.setter
    def failed_tests(self, tests_list):
        self._failed_tests = tests_list
        
    @property
    def pending_tests(self):
        return self._pending_tests
    
    @pending_tests.setter
    def pending_tests(self, tests_list):
        self._pending_tests = tests_list
    
    def clear_state(self):
        self.tests = {}
    


class VerboseReporter(object):
    def report_test_started(self, test):
        print("Started test '{0}'".format(test))
    
    def report_test_finished(self, test, e=None):
        if e:
            print("Test '{0}' failed: {1}".format(test, e))
        else:
            print("Test '{0}' passed".format(test))
    
    def report_all_finished(self, passed, failed, ran):
        print({"PASSED": passed,
                "FAILED": failed,
                "RAN": ran})
    


class FailReporter(object):
    def report_test_started(self, x=None):
        pass
    
    def report_test_finished(self, test, e=None):
        if e:
            print("test '{0}' failed: {1}".format(test, e))
        else:
            print(".")
    def report_all_finished(self, passed, failed, ran):
        print({"PASSED": passed,
                "FAILED": failed,
                "RAN": ran})



if __name__ == "__main__":
    my_runner = TestRunnerReporter(VerboseReporter())
    my_runner.add_test(test_assert_equal)
    my_runner.add_test(test_assert_is_none)
    my_runner.add_test(test_assert_not_equal)
    my_runner.run()
    print(my_runner.passed_tests)
    
