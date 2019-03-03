import numpy as np

test_case_1 = [0,1,2,4]
test_case_2 = [-1, -1, 1, 2, 3, 4, 4, 5, 7, 9, 14]
test_case_3 = [-165, -1, 1, 2, 3, 4, 4, 5,6, 7, 9, 14867678]
test_case_4 = [-1, -4, 3, 12, 565] * 5096

test_case_5 = list(range(-10000,0))*9 + list(range(0,98790))*140 \
            + list(range(98790,999987))*1 \
            + list(range(999988,3296409))*5

test_case_6 = [-1, -1, -1, -1] * 4000000
test_case_7 = [0] * 16830000

test_case_8 = list(range(-2**24,3)) \
            + list(range(4,9)) \
            + list(range(10,72))
            
test_case_9 = list(range(-2**20, 2**20  ))
