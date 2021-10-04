from hashing import encrypt
import checks
def addToIndex(username, password):
    result = checks.check(username, password, False)
    # print(result)
    if result.accepted:
        password = encrypt(password)
        with open("data.txt", "a") as f:
            f.write(f"{username}-{password}\n")
    return result
    
