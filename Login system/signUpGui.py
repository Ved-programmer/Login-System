from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar,Tk
import utility
import tkinter.font as tkFont

from hashing import encrypt
import checks
def addToIndex(username, password):
    result = checks.check(username, password, False)
    # print(result)
    if result.accepted:
        password = encrypt(password)
        with open("data.txt", "a") as f:
            f.write(f"{username}-{password}\n")
    return result
    

def check():
    global signUpMessage
    result = addToIndex(username.get(), password.get())
    try:signUpMessage.grid_forget()
    except Exception:pass
    if result.accepted:signUpMessage = Label(frame, text = "created account", font = messageHeight)
    else:signUpMessage = Label(frame, text = result.message, font = messageHeight)
    signUpMessage.grid(row = 2, column = 1)

def main(root, WIDTH, HEIGHT, wu, hu):

    #Initialization
    global frame, username, password, packs
    global messageHeight
    messageHeight = tkFont.Font(size = -int(HEIGHT/20))

    root.title("Sign Up")
    packs = []

    #Setting Heading and Frame
    utility.headingDesign("Sign up", packs, root, HEIGHT)
    frame = utility.formFrameDesign(root, packs, WIDTH)

    #Labels
    utility.entranceLabelDesign(frame, "username: ", 0, 0, HEIGHT)
    utility.entranceLabelDesign(frame, "password: ", 1, 0, HEIGHT)

    #Inputs
    username = utility.entranceDesign(frame, 0, 1, HEIGHT)
    password = utility.entranceDesign(frame, 1, 1, HEIGHT)

    submitButton = Button(frame, text = "Sign Up", command = check, font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    submitButton.grid(row = 2, column = 0)

    goBack = Button(frame, text = "go back", command = lambda : utility.back(packs, root), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    goBack.grid(row = 3, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = utility.basicStructure(612, 378, 1, "Delete Account")
    main(root, 612, 378, 612/1000, 378/1000)
