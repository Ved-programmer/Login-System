import checks
def passChange(username, oldPassword, newPassword):#TODO: The password Changing functionality
    check = checks.check(username, newPassword, True)
    if check.accepted:
        if checkIfPasswordsMatch(username, oldPassword):
            check.message = "Either the username or the password is incorrect";return check
        setPassword(username, newPassword)


    return check


def setPassword(username, newPassword):
    pass

def checkIfPasswordsMatch(username, password):
    return None