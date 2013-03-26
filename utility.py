
def print_and_assert(expression_text, operator, expression_output, assert_value):
    print '%s => %s' % (expression_text, expression_output)
    assert(operator(expression_output, assert_value))

def equal(a,b):
    return a == b

def print_and_assert_equal(function_output, true_value):
    print_and_assert('equality check', equal, function_output, true_value)
