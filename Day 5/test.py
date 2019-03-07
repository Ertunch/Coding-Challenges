"""Your algorithms' timing can be tested here.
Use _timing_wrapper() function to create a timed instance of your function
and use numbered test cases as input."""

import sys
try:
    sys.path.append('./Day 5')
except:
    pass
from funcs import *
from test_cases import *
from utils import _timing_wrapper

test = _timing_wrapper(decode)
test(TEST_CASE_1)
test(TEST_CASE_2)
test(TEST_CASE_3)
test(TEST_CASE_4)
test(TEST_CASE_5)
test(TEST_CASE_6)
test(TEST_CASE_7)
test(TEST_CASE_8)
test(TEST_CASE_9)
test(TEST_CASE_10)
