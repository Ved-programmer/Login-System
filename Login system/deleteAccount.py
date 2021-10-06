import hashing
import backEndUtilityFuncs
def delete(username, password):
    if backEndUtilityFuncs.checkIfCorrect(username, password):
        with open("data.txt", "r") as f:
            lines = f.readlines()
        try:lines.remove(f"{username}-{hashing.encrypt(password)}\n")
        except Exception:lines.remove(f"{username}-{hashing.encrypt(password)}")
        with open("data.txt", "w") as f:
            for i in lines:
                f.write(i)
        return True
    return False
    
