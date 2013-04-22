import pdb

RETRY_AMOUNT = 10

class InferenceProblem:
    #variables that might appear in partial_data
    variables = []
    partial_data = []

    def __init__(self, initial_variables, initial_partial_data):
        self.variables = initial_variables
        self.partial_data = initial_partial_data

def substitute(partial_data, bindings):
    """
    replace variables in the abstraction with the matching values in the bindings
    and return the resulting list
    """
    complete_list = []
    for element in partial_data:
        replacement = swap(element, bindings)
        complete_list += replacement
    return complete_list

def swap(element, bindings):
        if element in bindings.keys():
            return bindings[element]
        elif isinstance(element, list):
            return [substitute(element, bindings)]
        else:
            return [element]

import random

def is_symbol(thing):
    return not isinstance(thing, list)

def is_equivalent(abstraction1, abstraction2):
    bindings = match(abstraction1, abstraction2)
    #check if all bindings are single variables
    try:
        return all([is_variable(bound_values[0]) for bound_values
                    in bindings.values()])
    except (IndexError, AttributeError):
        return False


def abstract(data1, data2):
    if not isinstance(data1, list) or not isinstance(data2, list):
        if data1 == data2:
            return data1
        else:
            return variable_generator.generate()
    else:
        #both data are lists so iterate through abstracting the elements together
        def fast_forward(position_in_big, big_list, element_in_small):
              for new_position, element_in_big in enumerate(big_list[position_in_big:], start=position_in_big):
                  if element_in_big == element_in_small:
                      return new_position+1
              return None

        element_abstractions = []
        small_list,big_list = sorted([data1,data2], cmp=lambda x,y: len(x)-len(y))
        position_in_big = 0
        for position_in_small, element_in_small in enumerate(small_list):
            element_abstraction = abstract(element_in_small, big_list[position_in_big])
            element_abstractions.append(element_abstraction)
            if is_variable(element_abstraction):
                #fast forward position_in_big until the next element will match element_in_small
                #i.e. try and squeeze non-matching segments in the big list in between matching
                #parts of the small list
                new_position_in_big = fast_forward(position_in_big, big_list, element_in_small)
                if new_position_in_big is None:
                    position_in_big += 1
                else:
                    position_in_big = new_position_in_big
                    element_abstractions.append(element_in_small)
            else:
                position_in_big += 1
        #if there are more elements left in the big list bind them to a variable, observe
        #position_in_big was incremented one last time so we check it against len(big_list) instead
        #of len(big_list)-1 the position of the last element in big_list
        if position_in_big < len(big_list) and not is_variable(element_abstractions[-1]):
            element_abstractions.append(variable_generator.generate())
        return element_abstractions

class VariableGenerator:
    def __init__(self):
       self._counter = 0

    def generate(self):
      new_variable = 'v'+str(self._counter)
      self._counter += 1
      return new_variable

variable_generator = VariableGenerator()

def match(data1, data2):
    return match_with_retries(data1, data2, RETRY_AMOUNT)

def match_with_retries(data1, data2, retries):
    if is_variable(data1):
        return {data1: data2}
    elif is_variable(data2):
        return {data2: data1}
    elif is_symbol(data1) or is_symbol(data2):
        if data1 == data2:
            return {}
        else:
            if retries > 0:
                return match_with_retries(data1, data2, retries-1)
            else:
                return None
    else:
        assert(isinstance(data1, list) and isinstance(data2, list))
        #using a dictionary b/c has reference passed into functions allowing changes to be permanent after
        #exiting the function
        matches = []
        data1_position = 0
        data2_position = 0
        #iterate until one of the data has been examined completely
        while data1_position < len(data1) and data2_position < len(data2):
            #in the case where you can match a variable to a sublist of the other data
            #fast-forward the position in the other data
            if is_variable(data1[data1_position]) and data1_position < len(data1)-1:
                data2_position, matches = bind_variable(data1_position, data1,
                                                        data2_position, data2,
                                                        matches)
                data1_position += 2
            elif is_variable(data1[data1_position]):
                #the last element of data1 is a variable so bind it to the rest of data2
                matches.append(match(data1[data1_position], data2[data2_position:]))
                data1_position += 1
                data2_position = len(data2)
            elif is_variable(data2[data2_position]) and data2_position < len(data2)-1:
                data1_position, matches = bind_variable(data2_position, data2,
                                                        data1_position, data1,
                                                        matches)
                data2_position += 2
            elif is_variable(data2[data2_position]):
                #the last element of data2 is a variable so bind it to the rest of data1
                matches.append(match(data1[data1_position:], data2[data2_position]))
                data2_position += 1
                data1_position = len(data1)
            else:
                matches.append(match(data1[data1_position],
                                              data2[data2_position]))
                data1_position += 1
                data2_position += 1

        if data1_position < len(data1) or data2_position < len(data2):
            if data1_position < len(data1) and is_variable(data1[data1_position]):
                matches.append({data1[data1_position]: []})
            elif data2_position < len(data2) and is_variable(data2[data2_position]):
                matches.append({data2[data2_position]: []})
            else:
                if retries > 0:
                    return match_with_retries(data1, data2, retries-1)
                else:
                    return None
        if None in matches:
            if retries > 0:
                return match_with_retries(data1, data2, retries-1)
            else:
                return None
        else:
            #TODO handle case of same variable appearing in multiple places in the list
            all_bindings = {}
            for bindings in matches:
                all_bindings = dict(all_bindings.items() + bindings.items())
            return all_bindings

def bind_variable(variable_position, variable_data, other_position, other_data, matches):
    """
    Function for matching the variable in one data to some subset of the other data
    Fast forwards other_position and changes matches
    """

    def find_matching_positions():
        element_after_variable = variable_data[variable_position+1]
        possible_positions = {}
        for new_position, other_element in enumerate(other_data[other_position:], other_position):
            #we record the matches in case other_element is a variable, if the corresponding
            #position is chosen we can add the match to matches
            possible_match = match(element_after_variable, other_element)
            if possible_match is not None:
                possible_positions[new_position] = possible_match
        return possible_positions

    variable = variable_data[variable_position]
    element_after_variable = variable_data[variable_position+1]
    #find the possible matching positions in nonvariable data and possible bindings if
    #the matching position corresponds to a variable
    matching_positions = find_matching_positions()
    #randomly choose a match if one exists
    if len(matching_positions) > 0:
        chosen_match_position = random.choice(matching_positions.keys())
        #binding for elements right after what is bound to variable_position variable
        matches.append(matching_positions[chosen_match_position])
        #binding for variable_position variable
        matches.append({variable: other_data[other_position:chosen_match_position]})
        other_position = chosen_match_position+1
    else:
        matches.append(None)
    return other_position, matches

def is_variable(thing):
    return isinstance(thing, str) and (thing[0] == 'v' or thing[0] == 'x') \
      and thing[1:].isdigit()

from time import time
class Agent:
    def __init__(self):
        self.memory = Memory()

    def solve(self, inference_problem):
        def find_lowest_match(top_abstraction, inference_problem):

            leaves = []
            def traverse(abstraction_set, depth):
                match = abstraction.match(abstraction_set, inference_problem.partial_data)
                if match == None:
                    return None
                elif abstraction_set.get_children() == []:
                    leaves.append((match, depth))
                    return True
                else:
                    child_matches = [traverse(child_abstraction_set, depth+1) for child_abstraction_set
                                     in abstraction_set.get_children()]
                    if not any(child_matches):
                        leaves.append(match, depth)
                        return True
                    else:
                        return None

            traverse(top_abstraction, 0)
            sorted_leaves = sorted(leaves, key=lambda leaf: leaf[1])
            for possible_match in sorted_leaves:
                if all([is_primitive(possible_match[variable]) for variable in inference_problem.variables]):
                    return possible_match
            return sorted_leaves[0]

        possible_solutions = []
        for top_abstraction in self.memory.top_abstractions:
            possible_solutions.append(find_lowest_match(top_abstraction, inference_problem.partial_data))

        return get_least_abstract_match(possible_solutions)

    def solve_within(self, inference_problem, duration=None):
        start = time()
        while time()-start < duration:
            solution = self.solve(inference_problem)
            if solution is not None:
                break
        return solution

def is_primitive(thing):
    return not is_variable(thing) and not isinstance(thing, list)

def get_variables(partial_data):
    if is_variable(partial_data):
        return set([partial_data])
    elif not isinstance(partial_data, list):
        return set([])
    else:
        return set([]).union(*[get_variables(element) for element in partial_data])

class AbstractionSet:
    def __init__(self, abstraction, elements=set([]), parent=None, root=None):
        #set of AbstractionSets
        self.elements = elements
        self.abstraction = abstraction
        self.parent = parent
        self.root = root
        if self.root is None:
            self.root = self


    def contains(self, abstraction_set):
        binding = match(self.abstraction, abstraction_set.abstraction)
        return binding is not None and set(binding.keys()) == get_variables(self.abstraction)

    def get_parent(self):
        return self.parent

    def get_siblings(self):
        if self.parent is not None:
            return self.parent.get_children() - set([self])
        else:
            return set([])

    def get_children(self):
        return self.elements

    def insert(self, abstraction_set):
        if not is_equivalent(self.abstraction, abstraction_set.abstraction) and self.contains(abstraction_set):
            if any([child_abstraction_set.insert(abstraction_set) for child_abstraction_set in
                    self.elements]):
                return True
            else:
                self.elements.add(abstraction_set)
                abstraction_set.parent = self
                abstraction_set.root = self.root
                #see if any siblings should be moved into the new abstraction_set and adjust the
                #links if necessary
                siblings = abstraction_set.get_siblings()
                for sibling in siblings:
                    if abstraction_set.insert(sibling):
                        self.elements.remove(sibling)
                return True
        else:
            return False


    def create_new_abstractions_and_reorganize(self):
        parent = self.get_parent()
        siblings = self.get_siblings()
        for sibling in siblings:
            new_abstraction = abstract(sibling.abstraction, self.abstraction)
            if new_abstraction:
                #reorganize
                #elements for new_abstraction_set will be set during insertion
                new_abstraction_set = AbstractionSet(abstraction=new_abstraction,
                                                     elements=set([]))
                self.root.insert(new_abstraction_set)

    def __str__(self):
        return '(%s, %s)' % (str(self.abstraction), [str(element) for element in self.elements])

    def pretty_print(self):
        print self.pretty_hierarchy(0)

    def pretty_hierarchy(self, level):
        output = '\n'
        output += '*' * level
        output += ' %s' % self.abstraction
        for element in self.elements:
            output += element.pretty_hierarchy(level+1)
        return output
