"""
Provide an implementation for zip function using list comprehensions.
zip([1, 2, 3], ["a", "b", "c"])
[(1, "a"), (2, "b"), (3, "c")]
"""

def zip(lst1, lst2):
    return [(lst1[i], lst2[i]) for i in range(len(lst1))]

assert zip([1, 2, 3], ["a", "b", "c"]) == [(1, "a"), (2, "b"), (3, "c")]

"""
Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.

def square(x): return x * x
map(square, range(5))
[0, 1, 4, 9, 16]
"""

def map(func, lst):
    return [func(i) for i in lst]

def square(x): return x * x

assert map(square, range(5)) == [0,1,4,9,16]

"""
Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

def even(x): return x %2 == 0

filter(even, range(10))
[0, 2, 4, 6, 8]
"""

def filter(func, lst):
    return [i for i in lst if func(i)]

def even(x): return x %2 == 0

assert filter(even, range(10)) == [0, 2, 4, 6, 8]

"""
Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.

triplets(5)
[(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
"""

def triplets(n):
    triples = [(x,y,z) for x in range(1, n) for y in range(x,n) for z in range(
        y,n) if x+y==z]
    return triples

assert triplets(5) == [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]

"""
Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

enumerate(["a", "b", "c"])
[(0, "a"), (1, "b"), (2, "c")]

"""

def enumerate(lst):
    return [(i, lst[i]) for i in range(len(lst))]

assert enumerate(["a", "b", "c"]) == [(0, "a"), (1, "b"), (2, "c")]

"""
Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

a = array(2, 3)
 a
[[None, None, None], [None, None, None]]
>>> a[0][0] = 5
[[5, None, None], [None, None, None]]
"""

def array(dim1, dim2):
    lst = [[None for i in range(dim2)] for j in range(dim1)]
    return lst

assert array(2,3) == [[None, None, None], [None, None, None]]