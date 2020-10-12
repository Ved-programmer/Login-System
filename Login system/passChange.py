import checks
import hashing

def passChange(username, oldPassword, newPassword):#TODO: The password Changing functionality
    check = checks.check(username, newPassword, True)
    if check.accepted:
        if checkIfPasswordsMatch(username, oldPassword):setPassword(username, newPassword)
        else:return checks.message(False, "Either the username or the password is incorrect")
    return check


def setPassword(username, password):
    hashed = hashing.revert_back(hashing.increaseStringSize(password), hashing.logic(password))
    index, _ = getLineNum(username)
    newLine = f"{username}-{hashed}"
    with open("data.txt", "r") as f:
        lines = f.readlines()
    lines[index] = newLine
    with open("data.txt", "w") as f:
        for i in lines:
            f.write(i)

def checkIfPasswordsMatch(username, password):
    hashed = hashing.revert_back(hashing.increaseStringSize(password), hashing.logic(password))
    curPassword = getLineNum(username)[1].split("-")[1]
    if curPassword[-1:] == "\n":curPassword = curPassword[:-1]
    return hashed == curPassword

def getLineNum(username):
    with open("data.txt", "r") as f:data = f.readlines()
    for i, d in enumerate(data):
        if d.split("-")[0] == username:return [i, d]
    return [-1, ""]
