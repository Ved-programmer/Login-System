import checks
import hashing
import backEndUtilityFuncs

def passChange(username, oldPassword, newPassword):
    check = checks.check(username, newPassword, True)
    if check.accepted:
        if backEndUtilityFuncs.checkIfCorrect(username, oldPassword):setPassword(username, newPassword)
        else:return checks.message(False, "Either the username or the password is incorrect")
    return check


def setPassword(username, password):
    hashed = hashing.encrypt(password)
    index, _ = backEndUtilityFuncs.getLine(username)
    newLine = f"{username}-{hashed}"
    with open("data.txt", "r") as f:
        lines = f.readlines()
    lines[index] = newLine
    with open("data.txt", "w") as f:
        for i in lines:
            f.write(i)
