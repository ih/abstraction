
from abstraction import *
from utility import *
#note all AbstractionSet's created without the elements specified will share the same set object
root = AbstractionSet(abstraction=[[1, 'v0'], 'v1'], elements=set([]))
print_and_assert('root', equal, str(AbstractionSet(abstraction=[[1, 'v0'], 'v1'], elements=set([]))), "([[1, 'v0'], 'v1'], [])")
print_and_assert("root.insert(AbstractionSet(abstraction=[[1, 1, 'v9', 0, 0, 'v10'], 1], elements=set([])))", equal,
                 root.insert(AbstractionSet(abstraction=[[1, 1, 'v9', 0, 0, 'v10'], 1], elements=set([]))), True)
print_and_assert('root', equal, str(root), """([[1, 'v0'], 'v1'], ["([[1, 1, 'v9', 0, 0, 'v10'], 1], [])"])""")
print_and_assert("root.insert(AbstractionSet(abstraction=[[1, 1, 1, 0, 0, 0], 1], elements=set([])))", equal,
                 root.insert(AbstractionSet(abstraction=[[1, 1, 1, 0, 0, 0], 1], elements=set([]))), True)
print_and_assert('root', equal,
                 str(root), """([[1, 'v0'], 'v1'], ["([[1, 1, 'v9', 0, 0, 'v10'], 1], ['([[1, 1, 1, 0, 0, 0], 1], [])'])"])""")
root.insert(AbstractionSet(abstraction=[[1, 1, 0, 0], 1], elements=set([])))
print root
print_and_assert('root.insert(AbstractionSet(abstraction=[[1, 1, 0, 0], 1], elements=set([])))', equal,
                 str(root),"""([[1, 'v0'], 'v1'], ["([[1, 1, 'v9', 0, 0, 'v10'], 1], ['([[1, 1, 1, 0, 0, 0], 1], [])', '([[1, 1, 0, 0], 1], [])'])"])""")
root.insert(AbstractionSet(abstraction=[[1, 'v0'], 0], elements=set([])))
print_and_assert('root', equal,
                 str(root), """([[1, 'v0'], 'v1'], ["([[1, 'v0'], 0], [])", "([[1, 1, 'v9', 0, 0, 'v10'], 1], ['([[1, 1, 1, 0, 0, 0], 1], [])', '([[1, 1, 0, 0], 1], [])'])"])""")
root.insert(AbstractionSet(abstraction=[[1], 0], elements=set([])))
print root

#sibling test
parent = AbstractionSet(abstraction=[[1, 'v0'], 'v1'], elements=set([]))
child1 = AbstractionSet(abstraction=[[1, 1, 'v9', 0, 0, 'v10'], 1], elements=set([]))
child2 = AbstractionSet(abstraction=[[1, 'v0'], 0], elements=set([]))
parent.insert(child1)
parent.insert(child2)

print_and_assert('[str(sibling) for sibling in  child1.get_siblings()]', equal, [str(sibling) for sibling in  child1.get_siblings()], """["([[1, 'v0'], 0], [])"]""")
print_and_assert('[str(sibling) for sibling in  child2.get_siblings()]', equal, [str(sibling) for sibling in  child2.get_siblings()], """["([[1, 1, 'v9', 0, 0, 'v10'], 1], [])"]""")
