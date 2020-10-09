from hashing import *
import checks
def addToIndex(username, password):
    result = checks.check(username, password, False)
    if result.accepted:
        password = revert_back(increaseStringSize(password),logic(password))
        with open("data.txt", "a") as f:
            f.write(f"{username}-{password}\n")
    return result
