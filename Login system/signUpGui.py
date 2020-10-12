from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar,Tk
import signUp
import guiUtilityFuncs

def check():
    global signUpMessage
    result = signUp.addToIndex(username.get(), password.get())
    try:signUpMessage.grid_forget()
    except Exception:pass
    if result.accepted:signUpMessage = Label(frame, text = "created account")
    else:signUpMessage = Label(frame, text = result.message)
    signUpMessage.grid(row = 2, column = 1)

def main(root):

    #Initialization
    global frame, username, password, packs
    root.title("Sign Up")
    packs = []

    #Setting Heading and Frame
    guiUtilityFuncs.headingDesign("Sign up", packs, root)
    frame = guiUtilityFuncs.formFrameDesign(root, packs)

    #Labels
    guiUtilityFuncs.entranceLabelDesign(frame, "username: ", 0, 0)
    guiUtilityFuncs.entranceLabelDesign(frame, "password: ", 1, 0)

    #Inputs
    username = guiUtilityFuncs.entranceDesign(frame, 0, 1)
    password = guiUtilityFuncs.entranceDesign(frame, 1, 1)

    submitButton = Button(frame, text = "submit", command = check)
    submitButton.grid(row = 2, column = 0)

    goBack = Button(frame, text = "go back", command = lambda : guiUtilityFuncs.back(packs, root))
    goBack.grid(row = 3, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = guiUtilityFuncs.basicStructure(612, 378, 1, "Delete Account")
    main(root)
