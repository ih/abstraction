import pdb
from abstraction import *
from utility import *
#note all AbstractionSet's created without the elements specified will share the same set object
def test_creation():
    root = AbstractionSet(abstraction=[[1, 'v0'], 'v1'], elements=set([]))
    print_and_assert('root', equal, str(root), "([[1, 'v0'], 'v1'], [])")
    as1 = AbstractionSet(abstraction=[[1, 1, 'v9', 0, 0, 'v10'], 1], elements=set([]))
    print_and_assert("root.insert(as1)", equal,
                 root.insert(as1), True)
    print_and_assert('as1.root == root', equal, as1.root == root, True)

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
def test_get_siblings():
    parent = AbstractionSet(abstraction=[[1, 'v0'], 'v1'], elements=set([]))
    child1 = AbstractionSet(abstraction=[[1, 1, 'v9', 0, 0, 'v10'], 1], elements=set([]))
    child2 = AbstractionSet(abstraction=[[1, 'v0'], 0], elements=set([]))
    parent.insert(child1)
    parent.insert(child2)
    print_and_assert('[str(sibling) for sibling in  child1.get_siblings()]', equal,
                     [str(sibling) for sibling in  child1.get_siblings()], """["([[1, 'v0'], 0], [])"]""")
    print_and_assert('[str(sibling) for sibling in  child2.get_siblings()]', equal,
                     [str(sibling) for sibling in  child2.get_siblings()], """["([[1, 1, 'v9', 0, 0, 'v10'], 1], [])"]""")

#create_new_abstractions_and_reorganize
def test_create_new_abstractions_and_reorganize():
    root = AbstractionSet(['v0'], set([]))
    first = AbstractionSet([[1], 0], set([]))
    second = AbstractionSet([[1, 1], 0], set([]))
    root.insert(first)
    root.insert(second)
    second.create_new_abstractions_and_reorganize()
    print_and_assert('inserting [[1], 0] and [[1, 1], 0]', equal, str(root), """(['v0'], ["([[1, 'v0'], 0], ['([[1, 1], 0], [])', '([[1], 0], [])'])"])""")
    third = AbstractionSet([[1,1,1,1,1], 0], set([]))
    root.insert(third)
    third.create_new_abstractions_and_reorganize()
    root.pretty_print()
    fourth = AbstractionSet([[1,1,0,0],1], set([]))
    root.insert(fourth)
    fourth.create_new_abstractions_and_reorganize()
    #print 'inserted fourth: %s' % root
    print 'inserted fourth'
    root.pretty_print()
    fifth = AbstractionSet([[1,1,1,0,0,0],1], set([]))
    root.insert(fifth)
    print 'inserted fifth'
    root.pretty_print()
    #pdb.set_trace()
    fifth.create_new_abstractions_and_reorganize()
    print 'created new abstraction via fifth'
    root.pretty_print()

def test_pretty_hierarchy():
    level1 = AbstractionSet(['v0'], set([]))
    print level1.pretty_hierarchy(0)
    first = AbstractionSet([[1], 0], set([]))
    second = AbstractionSet([[1, 1], 0], set([]))
    level2 = AbstractionSet(['v0'], set([first, second]))
    print level2.pretty_hierarchy(0)



test_create_new_abstractions_and_reorganize()
#test_pretty_hierarchy()
