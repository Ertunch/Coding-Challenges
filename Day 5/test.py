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
test(TEST_CASE_41)
test(TEST_CASE_42)
test(TEST_CASE_43)
test(TEST_CASE_44)
test(TEST_CASE_5)
test(TEST_CASE_6)
test(TEST_CASE_7)
test(TEST_CASE_8)
test(TEST_CASE_9)
test(TEST_CASE_10)
test(TEST_CASE_101)
test(TEST_CASE_102)
test(TEST_CASE_103)

test = _timing_wrapper(solve_partial)
test(TEST_CASE_1, verbose=0)
test(TEST_CASE_2, verbose=0)
test(TEST_CASE_3, verbose=0)
test(TEST_CASE_4, verbose=0)
test(TEST_CASE_41, verbose=0)
test(TEST_CASE_42, verbose=0)
test(TEST_CASE_43, verbose=0)
test(TEST_CASE_44, verbose=0)
test(TEST_CASE_5, verbose=0)
test(TEST_CASE_6, verbose=0)
test(TEST_CASE_7, verbose=0)
test(TEST_CASE_8, verbose=0)
test(TEST_CASE_9, verbose=0)
test(TEST_CASE_10, verbose=0)
test(TEST_CASE_101, verbose=0)
test(TEST_CASE_102, verbose=0)
test(TEST_CASE_103)
