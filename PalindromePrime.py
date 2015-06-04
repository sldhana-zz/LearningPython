def palindrome_prime(number):
    next_number = number + 1
    while True:
        if is_prime(next_number) and (str(next_number) == str(next_number)[::-1]):
            print next_number
            return next_number
        else:
            next_number += 1



def is_prime(number):
    current = number - 1
    while current > 1:
        if number % current == 0:
            return False
        else:
            current -= 1
    return True





palindrome_prime(13)
palindrome_prime(3)