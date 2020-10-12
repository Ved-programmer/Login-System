import deleteAccount
from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import guiUtilityFuncs

#Deleting Logic
def delete():
    global deleteMessage
    result = deleteAccount.delete(username.get(), password.get())
    try:deleteMessage.grid_forget()
    except Exception:pass
    if result:deleteMessage = Label(frame, text = "Deleted Account")
    else:deleteMessage = Label(frame, text = "Incorrect Username or Password")
    deleteMessage.grid(row = 2, column = 1)

def main(root):
    #Initialization
    global frame, username, password, packs
    root.title("Delete Account")
    packs = []

    #Heading and setting Frame
    guiUtilityFuncs.headingDesign("Delete Account", packs, root)
    frame = guiUtilityFuncs.formFrameDesign(root, packs)
    
    #Labels
    guiUtilityFuncs.entranceLabelDesign(frame, "username: ", 0, 0)
    guiUtilityFuncs.entranceLabelDesign(frame, "password: ", 1, 0)

    #Inputs
    username = guiUtilityFuncs.entranceDesign(frame, 0, 1)
    password = guiUtilityFuncs.entranceDesign(frame, 1, 1)

    submitButton = Button(frame, text = "delete Account", command = delete)
    submitButton.grid(row = 2, column = 0)
    
    goBack = Button(frame, text = "go back", command = lambda : guiUtilityFuncs.back(packs, root))
    goBack.grid(row = 3, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = guiUtilityFuncs.basicStructure(612, 378, 1, "Delete Account")
    main(root)

