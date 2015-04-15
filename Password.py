"""
Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module. The password will be considered strong
enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well
as containing one uppercase letter and one lowercase letter in it. The password contains only
ASCII latin letters or digits.
"""
import re
def good_password(password):
    password_len = len(password)

    if password_len < 10:
        return False
    else:
        if not re.search("\d", password):
           return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[a-z]", password):
            return False

    return True


print good_password('A1213pokl') == False
print good_password('bAse730onE') == True
print good_password('asasasasasasasaas') == False
print good_password('QWERTYqwerty') == False
print good_password('123456123456') == False
print good_password('QwErTy911poqqqq') == True