
from abstraction import *
from utility import *

pattern0 = [[[1], 0], [[1,1], 0], [[1,1,1,1,1], 0], [[1,1], 0]]
pattern1 = [[[1,1,0,0],1], [[1,1,1,0,0,0],1], [[1,1,1,1,0,0,0,0],1]]
more_pattern0 = [[[2,2], 0], [[3,3,3,3,3], 0], [[5,5,5,5,5,5,5], 0]]
questionable_pattern0 = [[[1,0,1,0,1,0,1,0], 0], [[1,2,3,1,2,3,1,2,3,1,2,3], 0]]

more_pattern1 = [[[5,5,5,6,6,6],1], [[3,3,2,2],1]]
classify_problem0 = InferenceProblem(['x0'],[[1,1,1,1], 'x0'])  
classify_problem1 = InferenceProblem(['x0'], [[1,1,1,0,0,0], 'x0'])
classify_problem2 = InferenceProblem(['x0'], [[1,1,1,1,1,1,1,1,1,1,1,1,1], 'x0'])
classify_problem3 = InferenceProblem(['x0'], [[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0], 'x0'])

completion_problem2 = InferenceProblem(['v0'], [[1,'v0'], 1])  
abstraction_set = AbstractionSet(abstraction = pattern0[0])
  
print abstraction_set

abstraction_set1 = AbstractionSet(abstraction = pattern0[1])

print abstraction_set1

children_sets = set([abstraction_set, abstraction_set1])
abstraction_set0_01 = AbstractionSet(abstraction = [[1, 'v0'], 0], elements=children_sets)
print abstraction_set0_01

abstraction_set2 = AbstractionSet(abstraction = pattern1[0])
print abstraction_set2

print abstract([[1, 1, 0, 0], 1], [[1, 'v0'], 0])

children_sets = set([abstraction_set0_01, abstraction_set2])
abstraction_set1_012 = AbstractionSet(abstraction = [[1, 'v0'], 'v1'], elements = children_sets)
print abstraction_set1_012

abstraction_set3 = AbstractionSet(abstraction = pattern1[1])
children_sets = set([abstraction_set2, abstraction_set3])
 
abstraction_set2_3 = AbstractionSet(abstraction = [[1, 1, 'v9', 0, 0, 'v10'], 1], elements
= children_sets)
print abstraction_set2_3

children_sets = set([abstraction_set0_01, abstraction_set2_3])
abstraction_set1_012 = AbstractionSet(abstraction = [[1, 'v0'], 'v1'], elements = children_sets)
print abstraction_set1_012

print match([[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0], 'x0'], [[1, 'v0'], 'v1'])
