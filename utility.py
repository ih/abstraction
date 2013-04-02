
def print_and_assert(expression_text, operator, expression_output, assert_value):
    print '%s => %s' % (expression_text, expression_output)
    try:
        assert(operator(expression_output, assert_value))
    except AssertionError:
        print 'Assertion failed, got %s instead of %s' % (str(expression_output), str(assert_value))

def equal(a,b):
    return a == b

def print_and_assert_equal(function_output, true_value):
    print_and_assert('equality check', equal, function_output, true_value)
