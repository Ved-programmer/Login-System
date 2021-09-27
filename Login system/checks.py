from backEndUtilityFuncs import usernameExists
def check(username, password, passChange):
    securePasswordChecks = [passLenCheck, containsProperChars]
    usernameChecks = [usernameCharCheck, usernameExistsCheck]

    for check in usernameChecks:
        result = check(username, passChange)
        if not result.accepted:return result

    for check in securePasswordChecks:
        result = check(password)
        if not result.accepted:return result
        
    return message(True, "Password accepted")

def passLenCheck(password):
    if len(password) < 8:return message(False, "The password needs to be\natleast 8 characters long")
    if len(password) > 50:return message(False, "The password must be\nless then 50 characters")
    return message(True, "The password is accepted")

def containsProperChars(password):
    number = symbol = upperCase = lowerCase = False
    if "-" in password:return message(False, "The password can't contain '-'")
    for i in password:
        try:
            int(i);number = True;continue
        except Exception:pass
        if i in list(r"""!@#$%^&*()_+={}[]:;'"<,>.?/\|`~"""):
            symbol = True;continue
        upperCase = i == i.upper() or upperCase
        lowerCase = i == i.lower() or lowerCase
    
    if number and symbol and upperCase and lowerCase:return message(True, "This password is accepted")
    return message(False, "The password must contain a number,\na symbol, an uppercase and\na lowercase letter.")

def usernameCharCheck(username, passChange = False):
    if "-" in username: return message(False, "Username can't contain '-'")
    return message(True, "Username accepted")

def usernameExistsCheck(username, passChange):
    if not passChange:
        try:assert not(usernameExists(username))
        except Exception:return message(False, f"The username {username} is unavailable,\nplease try a different username")
    else:
        try:assert usernameExists(username)
        except Exception:return message(False, f"The username {username} does not exist\nplease re-check this username")
    return message(True, "Username Available")

class message:
    def __init__(self, accepted, message):
        self.accepted = accepted
        self.message = message

    def __repr__(self):
        return f"""acceptance - {self.accepted}, message - {self.message}"""

