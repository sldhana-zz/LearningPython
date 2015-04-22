"""
Roman numerals come from the ancient Roman numbering system. They are
based on specific letters of the alphabet which are combined to
signify the sum (or, in some cases, the difference) of their values.
The first ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional
and does not include a zero. Roman numerals are based on combinations
of these seven symbols:

Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
More additional information about roman numerals can be found on the
Wikipedia article.

For this task, you should return a roman numeral using the specified
integer value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string.

Example:

checkio(6) == 'VI'
checkio(76) == 'LXXVI'
checkio(13) == 'XIII'
checkio(44) == 'XLIV'
checkio(3999) == 'MMMCMXCIX'

"""
from collections import OrderedDict

"""
If you look carefully, the dictionary is ordered and there are extra additions
to support the special rules of Roman Numerals for digits 4 and 9.

"""
conversion_dict = OrderedDict([
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
])

""" Since the dictionary above contains all the possible permutations, all we're
    doing is finding the best match and decrementing the number.
"""
def roman_numerals(num):
    converted = ""
    while num > 0:
        for k, v in conversion_dict.iteritems():
            if k < num or k == num:
                converted = converted + v
                num = num - k
                break

    print converted
    return converted

assert roman_numerals(44) == 'XLIV'
assert roman_numerals(6) == 'VI'
assert roman_numerals(76) == 'LXXVI'
assert roman_numerals(13) == 'XIII'
assert roman_numerals(3999) == 'MMMCMXCIX'