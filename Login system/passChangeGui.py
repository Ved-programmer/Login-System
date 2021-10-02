from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import passChange
import guiUtilityFuncs
import tkinter.font as tkFont

def change():
    global resultMessage
    result = passChange.passChange(username.get(), oldPassword.get(), newPassword.get())
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
    guiUtilityFuncs.headingDesign("Change Password", packs, root, HEIGHT)
    frame = guiUtilityFuncs.formFrameDesign(root, packs, WIDTH)

    #Labels
    guiUtilityFuncs.entranceLabelDesign(frame, "username: ", 0, 0, HEIGHT)
    guiUtilityFuncs.entranceLabelDesign(frame, "old password: ", 1, 0, HEIGHT)
    guiUtilityFuncs.entranceLabelDesign(frame, "new password: ", 2, 0, HEIGHT)

    #Inputs
    username = guiUtilityFuncs.entranceDesign(frame, 0, 1, HEIGHT)
    oldPassword = guiUtilityFuncs.entranceDesign(frame, 1, 1, HEIGHT)
    newPassword = guiUtilityFuncs.entranceDesign(frame, 2, 1, HEIGHT)

    submitButton = Button(frame, text = "Change Password", command = change, font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    submitButton.grid(row = 3, column = 0)

    goBack = Button(frame, text = "go back", command = lambda : guiUtilityFuncs.back(packs, root), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    goBack.grid(row = 4, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = guiUtilityFuncs.basicStructure(612, 378, 1, "Delete Account")
    main(root, 612, 378, 612/1000, 378/1000)
