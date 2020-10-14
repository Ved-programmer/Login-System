import hashing
def usernameExists(username):
    with open("data.txt", "r") as f:
        for i in f.readlines():
            if i == "\n":continue
            if i[:i.index("-")] == username:return True
    return False

def getLine(username):
    if not usernameExists(username):return False
    index = 0
    with open("data.txt", "r") as f:
        cur = f.readline()
        while cur.split("-")[0] != username:
            cur = f.readline()
            index += 1
        return [index, cur.removesuffix("\n")]
    return [-1, ""]

def checkIfCorrect(unhashed, hashed):
    return hashed == hashing.encrypt(unhashed)
                                    
