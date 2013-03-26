
from abstraction import *
from utility import *
pattern0 = [[[1], 0], [[1,1], 0], [[1,1,1,1,1], 0], [[1,1], 0]]
pattern1 = [[[1,1,0,0],1], [[1,1,1,0,0,0],1], [[1,1,1,1,0,0,0,0],1]]
classify_problem0 = InferenceProblem(['x0'],[[1,1,1,1], 'x0'])  
classify_problem1 = InferenceProblem(['x0'], [[1,1,1,0,0,0], 'x0'])

agent = Agent()
print 'classify_problem0 %s' % classify_problem0.partial_data

print_and_assert_equal(agent.solve(classify_problem0), None)

agent.memory.add(pattern0[0])

classify_problem0 = InferenceProblem(['x0'],[[1,1,1,1], 'x0'])  
classify_problem1 = InferenceProblem(['x0'], [[1,1,1,0,0,0], 'x0'])
print agent.memory.memory

print_and_assert_equal(agent.solve(classify_problem0), None)

agent.memory.add(pattern0[1])
print agent.memory.memory

print_and_assert_equal(agent.solve(classify_problem0), None)

print_and_assert_equal(abstract(agent.memory.memory[0], agent.memory.memory[1]), [[1, 'v0'], 0])

print match(classify_problem0.partial_data, [[1, 'v0'], 0])

print match(classify_problem0.partial_data, [[1, 'v1'], 0])
