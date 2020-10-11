import hashing
from checks import checkIfUsernameExists 
def delete(username, password):
    if not checkIfUsernameExists(username):return False
    value = getLine(username)
    hashedPassword = value[0].split("-")[1][:-1] if value[0].split("-")[1].endswith("\n") else value[0].split("-")[1]
    if hashing.revert_back(hashing.increaseStringSize(password), hashing.logic(password)) == hashedPassword:
        with open("data.txt", "r") as f:
            lines = f.readlines()
        lines.pop(value[1])
        with open("data.txt", "w") as f:
            for i in lines:
                f.write(i)
        return True
    return False

def getLine(username):
    with open("data.txt", "r") as f:
        cur = f.readline()
        index = 0
        while cur.split("-")[0] != username:
            cur = f.readline()
            index += 1
        return [cur, index]
