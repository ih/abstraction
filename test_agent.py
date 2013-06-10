from abstraction import *
from utility import *
import pdb

pattern0 = [[[1], 0], [[1,1], 0], [[1,1,1,1,1], 0], [[1,1], 0]]
pattern1 = [[[1,1,0,0],1], [[1,1,1,0,0,0],1], [[1,1,1,1,0,0,0,0],1]]
more_pattern0 = [[[2,2], 0], [[3,3,3,3,3], 0], [[5,5,5,5,5,5,5], 0]]
questionable_pattern0 = [[[1,0,1,0,1,0,1,0], 0], [[1,2,3,1,2,3,1,2,3,1,2,3], 0]]

more_pattern1 = [[[5,5,5,6,6,6],1], [[3,3,2,2],1]]
classify_problem0 = InferenceProblem(['x0'],[[1,1,1,1], 'x0'])
classify_problem1 = InferenceProblem(['x0'], [[1,1,1,0,0,0], 'x0'])
classify_problem2 = InferenceProblem(['x0'], [[1,1,1,1,1,1,1,1,1,1,1,1,1], 'x0'])
classify_problem3 = InferenceProblem(
    ['x0'], [[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0], 'x0'])

completion_problem2 = InferenceProblem(['v0'], [[1,'v0'], 1])


def test_solve():
    agent = Agent()
    agent.memory.add(pattern1[0])
    print_and_assert(
        'added pattern1[0]', lambda x,y: True, agent.memory.dump(),
        [[[1], 0], [[1, 1], 0], [[1, 1, 0, 0], 1], [[1, 'v0'], 0],
        [[1, 'v1'], 'v2'], [[1, 1, 'v3'], 'v4']])
    agent.memory.add(pattern1[1])
    print_and_assert(
        'added pattern1[1]', lambda x,y: True, agent.memory.dump(),
        [[[1], 0], [[1, 1], 0], [[1, 1, 0, 0], 1],
        [[1, 1, 1, 0, 0, 0], 1], [[1, 'v0'], 0], [[1, 'v1'], 'v2'],
        [[1, 1, 'v3'], 'v4'], [[1, 'v5'], 'v6'], [[1, 1, 'v7'], 'v8'],
        [[1, 1, 'v9', 0, 0, 'v10'], 1]])
    print agent.solve(classify_problem0)
    print agent.solve(classify_problem1)
    print agent.solve(classify_problem3)
    agent.memory.add(pattern0[1])
    print agent.memory.dump()
    print agent.solve(classify_problem0)
    print agent.solve(classify_problem1)
    print agent.solve(classify_problem3)
    agent.memory.add(pattern0[2])
    print agent.memory.dump()
    print agent.solve(classify_problem0)
    print agent.solve(classify_problem1)

    print agent.solve(classify_problem3)
    agent.memory.add(pattern0[0])
    print agent.memory.dump()
    print agent.solve(classify_problem3)
test_solve()
