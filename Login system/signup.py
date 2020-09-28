from hashing import *
def addToIndex(username, password):
    password = revert_back(increment(password),logic(password))
    with open("data.txt", "a") as f:
        f.write(f"{username}-{password}\n")