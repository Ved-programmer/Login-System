from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import tkinter.font as tkFont

import checks
import hashing
import utility


def setPassword(username, password):
    hashed = hashing.encrypt(password)
    index, _ = utility.getLine(username)
    newLine = f"{username}-{hashed}"
    with open("data.txt", "r") as f:
        lines = f.readlines()
    lines[index] = newLine
    with open("data.txt", "w") as f:
        for i in lines:
            f.write(i)

def passChange(username, oldPassword, newPassword):
    if oldPassword == newPassword:return checks.message(False, "The new password can't be the\nsame as the old password")
    check = checks.check(username, newPassword, True)
    if check.accepted:
        if utility.checkIfCorrect(username, oldPassword):setPassword(username, newPassword)
        else:return checks.message(False, "Either the username or\nthe password is incorrect")
    return check



def change():
    global resultMessage
    result = passChange(username.get(), oldPassword.get(), newPassword.get())
    try:resultMessage.grid_forget()
    except Exception:pass
    if result.accepted:resultMessage = Label(frame, text = "password changed", font = messageHeight)
    else:resultMessage = Label(frame, text = result.message, font = messageHeight)
    resultMessage.grid(row = 3, column = 1)

def main(root, WIDTH, HEIGHT, wu, hu):
    #Initialization
    global packs, username, oldPassword, newPassword, frame
    global messageHeight
    messageHeight = tkFont.Font(size = -int(HEIGHT/20))

    root.title("Change Password")
    packs = []

    #Setting Frame and heading
    utility.headingDesign("Change Password", packs, root, HEIGHT)
    frame = utility.formFrameDesign(root, packs, WIDTH)

    #Labels
    utility.entranceLabelDesign(frame, "username: ", 0, 0, HEIGHT)
    utility.entranceLabelDesign(frame, "old password: ", 1, 0, HEIGHT)
    utility.entranceLabelDesign(frame, "new password: ", 2, 0, HEIGHT)

    #Inputs
    username = utility.entranceDesign(frame, 0, 1, HEIGHT)
    oldPassword = utility.entranceDesign(frame, 1, 1, HEIGHT)
    newPassword = utility.entranceDesign(frame, 2, 1, HEIGHT)

    submitButton = Button(frame, text = "Change Password", command = change, font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    submitButton.grid(row = 3, column = 0)

    goBack = Button(frame, text = "go back", command = lambda : utility.back(packs, root), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    goBack.grid(row = 4, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = utility.basicStructure(612, 378, 1, "Delete Account")
    main(root, 612, 378, 612/1000, 378/1000)
