letter = "abcde fghijklmnopqrstuvwxyz"
letter += letter.upper() + "1234567890#!@$%^&*()[] <>?/;:`~<>,.'=_"
def revert_back(string, times):
    string = list(string)
    for i in range(len(string)):
        string[i] = letter[(letter.index(string[i]) + abs(times)) % len(letter)]
    return "".join(string)

def logic(string):
    length = len(string)
    final = length
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
            if i != 0:final += 2 * length + length // i - 1
            else:final += 2 * length + length // i + 1
        elif string[i] in list("#!@$%^&*()[] <>?/;:`~<>,.'=_"):
            final += final*final//length + 4
        else:
            final += 2
        
    return final


def increaseStringSize(string):
    length = len(string)
    final = list(string)
    final = list(" ".join(final))
    for i in range(1, length*2, 2):
        final.insert(i - 1, "")
        final[i - 1] = letter[(letter.index(final[i]) + len(final)) % len(letter) - 1]

    cur = "".join(final)
    increasedSizedString = ""
    for j in range(len(cur)):
        idx1 = (letter.index(cur[j]) + len(string)) % len(letter)
        idx2 = (letter.index(cur[j]) // len(string)) % len(letter)
        idx3 = abs(letter.index(cur[j]) - len(string)) % len(letter)
        idx4 = (letter.index(cur[j]) * len(string)) % len(letter)
        idx5 = (letter.index(cur[j]) + len(string) // (idx4+1)) % len(letter)
        increasedSizedString += cur[i] + letter[idx1] + letter[idx2] + letter[idx3] + letter[idx4] + letter[idx5]
    return increasedSizedString


    



