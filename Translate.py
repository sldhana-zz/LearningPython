def translate(number):
    """
    Use the number map below for numbers that follow a certain pattern.  For example,
    12 will uniquely be called twelve and cannot be formed dynamically.
    """
    number_map = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }


    #this will hold the string representation of the number
    translated = ""

    """
    the first check is to make sure the number is greater than 0.  We need to do this
    to ensure the loop ends
    """
    while number > 0:
        #first check if the number is the map, if so, return value and decrement it
        if number in number_map:
            translated += " " + number_map[number]
            number -= number
            break
        """
        the logic below are for numbers that aren't in the list above.  For example,
        if the number is 98, it will first get "90" from the number and map it to the
        list above.  Then, it takes 98 - 90 and uses the balance to form the rest of the string
        """
        if number <= 99:
            translated += " " + number_map[(number/10) * 10]
            number = number - (number/10) * 10
        elif number <= 999:
            translated += " " + number_map[(number/100)] + " hundred"
            number = number - (number/100 * 100)
        elif number >= 1000:
            translated += " " + number_map[(number/1000)] + " thousand"
            number = number - (number/1000 * 1000)

    """
    since we added a space in the string, it returns the string chopping off the first character.
    There is probably a better way to do this, but I didn't want to spend too much time on it
    """

    print translated[1:]
    return translated[1:]


translate(1003)
translate(905)
translate(99)
translate(11)
translate(5)
translate(10)