
from abstraction import *
from utility import *
import pdb

test1 =  match([[1, 1, 1, 1], 'v0'], [[1, 1, 1, 1], 0])
print test1
assert(test1 == {'v0': [0]})
test2_0 = match([1, 1, 1, 1], [1, 1, 1, 1, 1])
print test2_0
assert(test2_0 is None)
test2 = match([[1, 1, 1, 1], 'v0'], [[1, 1, 1, 1, 1], 0])
print test2
assert(test2 is None)

for i in range(10):
    test3 = match(['v0', 0, 'v1'], [1,0,1,0,1,0,0,1])
    print test3
    assert(test3 in [{'v0': [1], 'v1': [1, 0, 1, 0, 0, 1]},
                     {'v0': [1, 0, 1], 'v1': [1, 0, 0, 1]},
                     {'v0': [1, 0, 1, 0, 1], 'v1': [0, 1]},
                     {'v0': [1, 0, 1, 0, 1, 0], 'v1': [1]}])

pattern0 = [[[1], 0], [[1,1], 0], [[1,1,1,1,1], 0], [[1,1], 0]]
pattern1 = [[[1,1,0,0],1], [[1,1,1,0,0,0],1], [[1,1,1,1,0,0,0,0],1]]
abstraction = [[1, 1, 'v0', 0, 0, 'v1'], 1]
print match(abstraction, pattern1[0])
print match(abstraction, pattern1[1])

def fail_case():
    print 'case where algorithm can fail'
    for i in range(10):
        #a case where this algorithm can fail to find the existing valid binding
        test4 = match(['v0', 0], [1,0,1,0,1,0,0])
        print test4
        assert(test4 in [None, {'v0': [1, 0, 1, 0, 1, 0]}])
    
#the abstraction f
f = [[1, 'v0'], 'v1']
test5 = match(f, [[1,1],0])
print test5
assert(test5 == {'v0': [1], 'v1': [0]})

f = [[1, 'v0'], 'v1']
g = ['f', ['v0'], [0]]
h = ['f', [1, 'v1'], ['v2']]

test6 = match(f, pattern1[1])
print test6
assert(test6 == {'v0': [1, 1, 0, 0, 0], 'v1': [1]})
test7 = match(g, pattern1[1])
print test7
assert(test7 is None)
test8 = match(h, pattern1[1])
print test8
assert(test8 is None)

from abstraction import *;
pattern1_1 = ['f', [1, 1, 0, 0, 0], [1]]

g = ['f', ['v0'], [0]]
h = ['f', [1, 'v1'], ['v2']]

print_and_assert_equal(match(g, pattern1_1), None)
print_and_assert_equal(match(h, pattern1_1), {'v1': [1, 0, 0, 0], 'v2': [1]})

from abstraction import *
new_abstractions = [['v0', [1, 'v1'], ['v2']],
                    ['v3', ['v4'], ['v5']],
                    ['v6', [1, 0, 0, 'v7'], [1]]]
pattern0 = [['f', [], [0]], ['f', [1], [0]]]
pattern1 = [['f', [1, 0, 0], [1]], ['h', [1, 0, 0, 0], [1]]]

for pattern in pattern0:
    for abstraction in new_abstractions:
        print '%s,%s =>' % (abstraction, pattern)
        print match(abstraction, pattern)
        print '\n'

for pattern in pattern1:
    for abstraction in new_abstractions:
        print '%s,%s =>' % (abstraction, pattern)
        print match(abstraction, pattern)
        print '\n'


fail_case()
