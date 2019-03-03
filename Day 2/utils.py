from datetime import datetime
import numpy as np

# def _timing_wrapper(func):
#     def test(func, array, shuffle=True):
#         test_array = array.copy()
#         if shuffle:
#             np.random.shuffle(test_array)
#         tic = datetime.now()
#         func(test_array)
#         toc = datetime.now()
#         print('Function executed : %.5f seconds' % (toc-tic).total_seconds())
#     return test

def _timing_wrapper(func, *args):
    """Embeds function for a timing operation.
    Usage:
    >>>test = _timing_wrapper(func)
    >>>test(*func_args)
    """
    def timing(*args):
        # print(args)
        then = datetime.now()
        func(*args)
        now = datetime.now()
        print('Function executed : %.5f seconds' % (now-then).total_seconds())
    return timing
