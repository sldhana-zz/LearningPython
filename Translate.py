def translate(number):
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


    """
    number is 4
    """
    translated = ""

    while number > 0:
        if number in number_map:
            translated += " " + number_map[number]
            number -= number
        if number <= 0:
            break
        if number <= 10:
            translated += " " + number_map[number]
            number -= number
        elif number <= 99:
            translated += " " + number_map[(number/10) * 10]
            number = number - (number/10) * 10
        elif number <= 999:
            translated += " " + number_map[(number/100)] + " hundred"
            number = number - (number/100 * 100)
        elif number >= 1000:
            translated += " " + number_map[(number/1000)] + " thousand"
            number = number - (number/1000 * 1000)

    print translated[1:]
    return translated[1:]


translate(1003)
translate(905)
translate(99)
translate(11)
translate(5)