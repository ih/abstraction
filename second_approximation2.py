
from abstraction import *
from utility import *

pattern0 = [[[1], 0], [[1,1], 0], [[1,1,1,1,1], 0], [[1,1], 0]]
pattern1 = [[[1,1,0,0],1], [[1,1,1,0,0,0],1], [[1,1,1,1,0,0,0,0],1]]
classify_problem0 = InferenceProblem(['x0'],[[1,1,1,1], 'x0'])  
classify_problem1 = InferenceProblem(['x0'], [[1,1,1,0,0,0], 'x0'])
classify_problem2 = InferenceProblem(['x0'], [[1,1,1,1,1,1,1,1,1,1,1,1,1], 'x0'])
classify_problem3 = InferenceProblem(['x0'], [[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0], 'x0'])

completion_problem2 = InferenceProblem(['v0'], [[1,'v0'], 1])

agent = Agent()
print 'classify_problem0 %s' % classify_problem0.partial_data
print_and_assert_equal(agent.solve(classify_problem0), None)
agent.memory.add(pattern0[0])
print 'agent memory %s' % agent.memory.dump()
print_and_assert_equal(agent.solve(classify_problem0), None)
agent.memory.add(pattern0[1])
print 'agent memory %s' % agent.memory.dump()
print agent.solve(classify_problem0)

print 'classify_problem2 %s' % classify_problem2.partial_data
print agent.solve(classify_problem2)

print 'classify_problem3 %s' % classify_problem3.partial_data
print agent.solve(classify_problem3)

agent.memory.add(pattern1[0])
print 'agent memory %s' % agent.memory.dump()

agent.memory.add(pattern1[1])
print 'agent memory %s' % agent.memory.dump()

print match(classify_problem3.partial_data, [[1, 1, 'v9', 0, 0, 'v10'], 1])

print agent.solve(classify_problem3)

print 'completion_problem2 %s' % completion_problem2.partial_data
print agent.solve(completion_problem2)
assert agent.solve(completion_problem2) != None

classify_problem4 = InferenceProblem(['v0'], [[8,8,8,8,8], 'x0'])
classify_problem5 = InferenceProblem(['v0'], [[2,2,2,2,2,2,1,1,1,1,1,1], 'x0'])

classify_problem6 = InferenceProblem(['v0'], [[4,4,5,5,4,4,5,5,4,4,5,5], 'x0'])

completion_problem4 = InferenceProblem(['v0', 'v1'], [[5, 'x0', 6, 'x1'], 1])
completion_problem5 = InferenceProblem(['v0'], [['x0',9,9,9], 0])

completion_problem6 = InferenceProblem(['v0'], [[1,4,1,1,4,1,1,4,1,'x0',1,4,1], 'x0'])
completion_problem6 = InferenceProblem(['v0'], [[1,4,1,1,4,1,1,4,1,'x0'], 'x0'])

print 'current memory: %s' % agent.memory.dump()
print 'classify_problem4 %s' % classify_problem4.partial_data
print agent.solve(classify_problem4)

more_pattern0 = [[[2,2], 0], [[3,3,3,3,3], 0], [[5,5,5,5,5,5,5], 0]]
questionable_pattern0 = [[[1,0,1,0,1,0,1,0], 0], [[1,2,3,1,2,3,1,2,3,1,2,3], 0]]

more_pattern1 = [[[5,5,5,6,6,6],1], [[3,3,2,2],1]]

agent.memory.add(more_pattern0[0])
print 'agent memory: %s' % agent.memory.dump()

print 'classify_problem4 %s' % classify_problem4.partial_data
print agent.solve(classify_problem4)

print classify_problem3.partial_data
print agent.solve(classify_problem3)

print agent.memory.dump()
print 'adding more pattern0: %s' % more_pattern0[1]
agent.memory.add(more_pattern0[1])
print agent.memory.dump()

print agent.memory.dump()
print 'adding more pattern0: %s' % more_pattern0[2]
agent.memory.add(more_pattern0[2])
print agent.memory.dump()
