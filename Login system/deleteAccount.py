import hashing
import backEndUtilityFuncs
def delete(username, password):
    if not backEndUtilityFuncs.usernameExists(username):return False
    value = backEndUtilityFuncs.getLine(username)
    hashedPassword = value[1].split("-")[1].removesuffix("\n")
    if backEndUtilityFuncs.checkIfCorrect(password, hashedPassword):
        with open("data.txt", "r") as f:
            lines = f.readlines()
        lines.pop(value[0])
        with open("data.txt", "w") as f:
            for i in lines:
                f.write(i)
        return True
    return False

