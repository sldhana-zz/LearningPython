"""
In this mission you should write you own py3 implementation (but you can use py2
 for this) of the built-in functions min and max. Some builtin functions are closed
 here: import, eval, exec, globals. Don't forget you should implement two functions in your code.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.

If one positional argument is provided, it should be an iterable. The largest (smallest) item in the iterable is returned. If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.

The optional keyword-only key argument specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower).

If multiple items are maximal (minimal), the function returns the first one encountered.

-- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for the "min" function.
"""
import types

def min(*args, **kwargs):
    if len(args) == 0:
        return None
    # check if key exists in the keyword argument, if it does, we fall into
    # the first if
    if 'key' in kwargs:
        key = kwargs['key']
        lst = []
        # this is especially useful when the first param is usually a list
        # that contains other list.  The key could be a lambda function that
        # gets applied to each item in the arguments. Note the args[0] below
        if len(args) == 1:
            for i in args[0]:
                lst.append(key(i))
            return get_min(lst, args[0])
        else:
            # in this part, the argument is not a list, hence we just apply
            # the key to all items.
            for i in args:
               lst.append(key(i))
            return get_min(lst, args)
    elif len(args) == 1:
        # check if a list, if so, just pass it to the helper function
        if isinstance(args[0], list):
            return get_min(args[0])
        # check for tuples, generators, sets and strings, if it is, we convert
        # those types to a list
        elif isinstance(args[0], tuple) or isinstance(args[0],
                                                      types.GeneratorType) or\
                isinstance(args[0], set) or isinstance(args[0], str):
            return get_min(list(args[0]))

    else:
        # all else, just call helper
        return get_min(list(args))



def get_min(args, pair=[]):
    # we use this pair param when we have to do things like a lambda on the
    # original list.  The pair will hold the untouched list, the args will
    # contained the modified one for the purpose of calculation.
    min = args[0]
    pos = 0
    for k, v in enumerate(args[1:]):
        if v < min:
            min = v
            pos = k+1

    if len(pair) != 0:
        min = pair[pos]

    return min


def max(*args, **kwargs):
    if len(args) == 0:
        return None
    if 'key' in kwargs:
        key = kwargs['key']
        lst = []
        if len(args) == 1:
            for i in args[0]:
                lst.append(key(i))
            return get_max(lst, args[0])
        else:
            for i in args:
               lst.append(key(i))
            return get_max(lst, args)
    elif len(args) == 1:
        #check if a list
        if isinstance(args[0], list):
            return get_max(args[0])
        #check if it's a tuple. generator, set or string
        elif isinstance(args[0], tuple) or isinstance(args[0],
                                                      types.GeneratorType) or\
                isinstance(args[0], set) or isinstance(args[0], str):
            return get_max(list(args[0]))

    else:
        return get_max(list(args))



def get_max(args, pair=[]):
    max = args[0]
    pos = 0
    for k, v in enumerate(args[1:]):
        if v > max:
            max = v
            pos = k+1

    if len(pair) != 0:
        max = pair[pos]

    print max
    return max



assert max(3, 2) == 3
assert min(3, 2) == 2
assert max([1, 2, 0, 3, 4]) == 4
assert min("hello") == "e"
assert max(2.2, 5.6, 5.9, key=int) == 5.6
assert min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
assert min((9,)) == 9
assert min(abs(i) for i in range(-10, 10)) == 0
assert max(x + 5 for x in range(6)) == 10
assert max(filter(str.isalpha,"@v$e56r5CY{]")) == "v"