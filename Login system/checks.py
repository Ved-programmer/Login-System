def check(username, password, passChange): #The passChange functionality is not implemented yet 
    if not passChange:
        try:assert not(checkIfUsernameExists(username))
        except Exception:return message(False, f"The username {username} is unavailable, please try a different username")
    else:
        try:assert checkIfUsernameExists(username)
        except Exception:return message(False, f"The username {username} does not exist please re-check this username")
    
    securePasswordChecks = [passLenCheck, containsProperChars]
    for check in securePasswordChecks:
        result = check(password)
        if not result.accepted:return result
    return message(True, "Password accepted")

def passLenCheck(password):
    if len(password) < 8:return message(False, "The password needs to be atleast 8 characters long")
    return message(True, "The password is accepted")

def containsProperChars(password):
    number = symbol = upperCase = lowerCase = False
    for i in password:
        try:
            int(i);number = True;continue
        except Exception:pass
        if i in list("""!@#$%^&*()-_+={}[]:;'"<,>.?/\|`~"""):
            symbol = True;continue
        upperCase = i == i.upper() or upperCase
        lowerCase = i == i.lower() or lowerCase
    
    if number and symbol and upperCase and lowerCase:return message(True, "This password is accepted")
    return message(False, "The message must contain a number, a symbol, an uppercase and a lowercase letter.")


def checkIfUsernameExists(username):
    with open("data.txt", "r") as f:
        for i in f.readlines():
            if i == "\n":continue
            if i[:i.index("-")] == username:return True
    return False

class message:
    def __init__(self, accepted, message):
        self.accepted = accepted
        self.message = message

