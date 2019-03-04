"""Your algorithms timing can be tested here.
Use _timing_wrapper() function to create a timed instance of your function
and use numbered test cases as input."""

import sys
try:
    sys.path.append('./Day 2')
except:
    pass
from funcs import *
from test_cases import *
from utils import _timing_wrapper


test = _timing_wrapper(func1)
test(test_case_1)
test(test_case_2)
test(test_case_3)
test(test_case_4)
test(test_case_5)
test(test_case_6)
test(test_case_7)

test = _timing_wrapper(func3)
test(test_case_1)
test(test_case_2)
test(test_case_3)
test(test_case_4)
test(test_case_5)
test(test_case_6)
test(test_case_7)

test = _timing_wrapper(solution)
test(test_case_1)
test(test_case_2)
test(test_case_3)
test(test_case_4)
test(test_case_5)
test(test_case_6)
test(test_case_7)
