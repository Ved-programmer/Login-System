import deleteAccount
from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import guiUtilityFuncs
import tkinter.font as tkFont

#Deleting Logic
def delete():
    global deleteMessage
    result = deleteAccount.delete(username.get(), password.get())
    try:deleteMessage.grid_forget()
    except Exception:pass
    if result:deleteMessage = Label(frame, text = "Deleted Account", font = messageHeight)
    else:deleteMessage = Label(frame, text = "Incorrect Username or Password", font = messageHeight)
    deleteMessage.grid(row = 2, column = 1)

def main(root, WIDTH, HEIGHT, wu, hu):
    #Initialization
    global frame, username, password, packs
    global messageHeight
    messageHeight = tkFont.Font(size = -int(HEIGHT/20))

    root.title("Delete Account")
    packs = []

    #Heading and setting Frame
    guiUtilityFuncs.headingDesign("Delete Account", packs, root, HEIGHT)
    frame = guiUtilityFuncs.formFrameDesign(root, packs, WIDTH)
    
    #Labels
    guiUtilityFuncs.entranceLabelDesign(frame, "username: ", 0, 0, HEIGHT)
    guiUtilityFuncs.entranceLabelDesign(frame, "password: ", 1, 0, HEIGHT)

    #Inputs
    username = guiUtilityFuncs.entranceDesign(frame, 0, 1, HEIGHT)
    password = guiUtilityFuncs.entranceDesign(frame, 1, 1, HEIGHT)

    submitButton = Button(frame, text = "Delete Account", command = delete, font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    submitButton.grid(row = 2, column = 0)
    
    goBack = Button(frame, text = "Go back", command = lambda : guiUtilityFuncs.back(packs, root), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    goBack.grid(row = 3, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = guiUtilityFuncs.basicStructure(612, 378, 1, "Delete Account")
    main(root, 612, 378, 612/1000, 378/1000)

