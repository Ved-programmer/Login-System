import backEndUtilityFuncs

def login_or_not(username, password):
    hashed = backEndUtilityFuncs.getLine(username)
    if hashed == False:return False
    return backEndUtilityFuncs.checkIfCorrect(password, hashed[1].split("-")[1].removesuffix("\n"))
