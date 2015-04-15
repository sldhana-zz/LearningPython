"""
You are given a text, which contains different english letters and punctuation symbols.
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search,
"A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
"""
import collections
import operator


def most_wanted(str):
    # We want to first lowercase the string, then sort them.
    sorted_str = "".join(sorted(str.lower()))

    # Use a sorted dictionary here.  This shoves the item in the order you put it into the dictionary.
    dct = collections.OrderedDict()

    for i in sorted_str:
        if i.isalpha():
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1

    """
        dct.iteritems() returns an iterator over the dictionary's (key, value) pairs.
        operator module returns a set of functions.  In the code below, we're telling
        the operator to pass the "value" of the tuple (key, value) into the max function.
        The max function returns one item, out of which, we get the key of the tuple.
    """
    return max(dct.iteritems(), key=operator.itemgetter(1))[0]


print most_wanted("Hello World!") == "l"
print most_wanted("How do you do?") == "o"
print most_wanted("One") == "e"
print most_wanted("Oops!") == "o"
print most_wanted("AAaooo!!!!") == "a"
print most_wanted("abe") == "a"
