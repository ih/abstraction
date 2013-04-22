from abstraction import *
from utility import *
import pdb
def test_equivalent_with_nested_variables():
    a1 = [[1, 'v3'], 'v4']
    a2 = [[1, 'v7'], 'v8']
    print_and_assert("is_equivalent([[1, 'v3'], 'v4'], [[1, 'v7'], 'v8'])",
                     equal, is_equivalent(a1, a2), True)

def test_equivalent_with_no_variables():
    a1 = [[1, 1, 1, 1, 1], 0]
    a2 = [[1, 1, 1, 1, 1], 0]
    print_and_assert("is_equivalent([[1, 1, 1, 1, 1], 0], [[1, 1, 1, 1, 1], 0])",
                     equal, is_equivalent(a1, a2), True)

def test_non_equivalent_with_match():
    a1 = [[1, 'v3'], 'v4']
    a2 = [[1, 'v5'], 1]
    print_and_assert("is_equivalent([[1, 'v3'], 'v4'], [[1, 'v5'], 1])",
                     equal, is_equivalent(a1, a2), False)

test_equivalent_with_nested_variables()
test_equivalent_with_no_variables()
test_non_equivalent_with_match()
