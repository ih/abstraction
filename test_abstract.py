
from abstraction import *
pattern0 = [[[1], 0], [[1,1], 0], [[1,1,1,1,1], 0], [[1,1], 0]]
pattern1 = [[[1,1,0,0],1], [[1,1,1,0,0,0],1], [[1,1,1,1,0,0,0,0],1]]
abstraction = abstract(pattern1[0], pattern1[1])
print abstraction
assert(abstraction == [[1, 1, 'v0', 0, 0, 'v1'], 1])
abstraction2 = abstract(pattern0[0], pattern0[1])
print abstraction2
assert(abstraction2 == [[1, 'v2'], 0])
