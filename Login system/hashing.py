letter = """abcdefghijklmnopqrstuvwxyz"""
letter += letter.upper() + """1234567890#!@$%^&*()[] "<>?/;:`~,.'=_-"""
def revert_back(string, times):
    string = list(string)
    for i in range(len(string)):
        string[i] = letter[(letter.index(string[i]) + abs(times)) % len(letter)]
    return "".join(string)

def logic(string):
    length = len(string)
    final = length
    double = 2 * length
    for i in range(length):
        if string[i] == "0":
            final -= length - length // 3
        elif string[i] == "1":
            final += length - length // 3
        elif string[i] == "2":
            final += length - length // 4
        elif string[i] == "3":
            final -= length - length // 4
        elif string[i] in list("abcde fghijk,"):
            if i != 0:final += double + length // i - 1
            else:final += double + length // (i + 1)
        elif string[i] in list("#!@$%^&*()[] <>?/;:`~<>,.'=_"):
            final += final^2//length + 3
        else:
            final += 2
        
    return final


def increaseStringSize(string):
    final = ""
    
    for i in string:
        final += letter[(letter.index(i) + len(final)) % len(letter) - 1]

    cur = final
    increasedSizedString = ""

    for j in range(len(cur)):
        idx1 = (letter.index(cur[j]) + len(string)) % len(letter)
        if string[j] in "abcdefghijklmnopqrstuvwxyz .-'_=":idx2 = (letter.index(cur[j]) // len(string)) % len(letter)
        else:idx2 = letter.index(string[j]) + 2
        idx3 = abs(letter.index(cur[j]) - len(string)) % len(letter)
        increasedSizedString += letter[idx1] + letter[idx2] + letter[idx3]
    return increasedSizedString

def encrypt(string, encryptionLevel = 2):
    cur = string
    for _ in range(encryptionLevel):
        increasedStringSize = increaseStringSize(cur)
        stringLogic = logic(cur)
        cur = revert_back(increasedStringSize, stringLogic)
    return cur