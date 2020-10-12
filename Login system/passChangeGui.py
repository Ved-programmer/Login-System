from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import passChange
import guiUtilityFuncs

def change():
    global resultMessage
    result = passChange.passChange(username.get(), oldPassword.get(), newPassword.get())
    try:resultMessage.grid_forget()
    except Exception:pass
    if result.accepted:resultMessage = Label(frame, text = "password changed")
    else:resultMessage = Label(frame, text = result.message)
    resultMessage.grid(row = 5, column = 1)

def main(root):
    #Initialization
    global packs, username, oldPassword, newPassword, frame
    root.title("Change Password")
    packs = []

    #Setting Frame and heading
    guiUtilityFuncs.headingDesign("Change Password", packs, root)
    frame = guiUtilityFuncs.formFrameDesign(root, packs)

    #Labels
    guiUtilityFuncs.entranceLabelDesign(frame, "username: ", 0, 0)
    guiUtilityFuncs.entranceLabelDesign(frame, "old password: ", 1, 0)
    guiUtilityFuncs.entranceLabelDesign(frame, "new password: ", 2, 0)

    #Inputs
    username = guiUtilityFuncs.entranceDesign(frame, 0, 1)
    oldPassword = guiUtilityFuncs.entranceDesign(frame, 1, 1)
    newPassword = guiUtilityFuncs.entranceDesign(frame, 2, 1)

    submitButton = Button(frame, text = "submit", command = change)
    submitButton.grid(row = 3, column = 0)

    goBack = Button(frame, text = "go back", command = lambda : guiUtilityFuncs.back(packs, root))
    goBack.grid(row = 4, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = guiUtilityFuncs.basicStructure(612, 378, 1, "Delete Account")
    main(root)
