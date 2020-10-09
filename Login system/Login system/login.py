from hashing import *

def getVal(username):
    with open("data.txt", "r") as f:
        cur = f.readline()
        while cur.split("-")[0] != username:
            cur = f.readline()
        return cur.split("-")[1]

def check_if_correct(cur_password, hashed_password):
    converted = revert_back(increaseStringSize(cur_password), logic(cur_password))
    return converted == hashed_password[:-1]


def login_or_not(username, password):
    hashed = getVal(username)
    return check_if_correct(password, hashed)