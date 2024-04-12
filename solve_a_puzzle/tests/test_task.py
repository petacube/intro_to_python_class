import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from tuples import my_tuple
output = f.getvalue().split('\n')
result_1 = output[0]
result_2 = output[1]


class TestCase(unittest.TestCase):
    def test_len(self):
        input_arr=[1,2,3]
        target=5
        sum_indx = compute_brute_force_indexes(input_arr,target)
        self.assertTrue(sum_indx == [1,2],msg="Are your indexes correct")
        sum_indx = compute_via_hash_indexes(input_arr,target)
        self.assertTrue(sum_indx == [1,2],msg="Are your indexes correct")

    def test_tuple(self):
