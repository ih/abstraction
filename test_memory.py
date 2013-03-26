
from abstraction import *
from utility import *

pattern0 = [[[1], 0], [[1,1], 0], [[1,1,1,1,1], 0], [[1,1], 0]]
pattern1 = [[[1,1,0,0],1], [[1,1,1,0,0,0],1], [[1,1,1,1,0,0,0,0],1]]

agent = Agent()
agent.memory.add(pattern0[0])
print_and_assert_equal(agent.memory.dump(), [pattern0[0]])
agent.memory.add(pattern0[1])
print_and_assert_equal(agent.memory.dump(), [[[1], 0], [[1, 1], 0], [[1, 'v0'], 0]])
agent.memory.add(pattern1[0])
print_and_assert_equal(agent.memory.dump(), [[[1], 0], [[1, 1], 0], [[1, 1, 0, 0], 1], [[1, 'v0'], 0], [[1, 'v1'], 'v2'], [[1, 1, 'v3'], 'v4']])
agent.memory.add(pattern1[1])
print_and_assert_equal(agent.memory.dump(), [[[1], 0], [[1, 1], 0], [[1, 1, 0, 0], 1], [[1, 1, 1, 0, 0, 0], 1], [[1, 'v0'], 0], [[1, 'v1'], 'v2'], [[1, 1, 'v3'], 'v4'], [[1, 'v5'], 'v6'], [[1, 1, 'v7'], 'v8'], [[1, 1, 'v9', 0, 0, 'v10'], 1]])
