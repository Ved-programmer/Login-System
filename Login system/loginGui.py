from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import login
import guiUtilityFuncs
import tkinter.font as tkFont

#Login Logic
def check():
    global loginMessage

    try:loginMessage.grid_forget()
    except Exception:pass

    if login.login_or_not(username.get(), password.get()):
        loginMessage = Label(frame, text = "you are now logged in", font = messageHeight)
    else:
        loginMessage = Label(frame, text = "incorrect username or password", font = messageHeight)

    loginMessage.grid(row = 2, column = 1)

def main(root, WIDTH, HEIGHT, wu, hu):
    #Initialization
    global frame, username, password, packs
    global messageHeight
    messageHeight = tkFont.Font(size = -int(HEIGHT/20))
    
    root.title("Log In")
    packs = []

    #Setting Heading and Frame
    guiUtilityFuncs.headingDesign("Log In", packs, root, HEIGHT)
    frame = guiUtilityFuncs.formFrameDesign(root, packs, WIDTH)

    #Labels
    guiUtilityFuncs.entranceLabelDesign(frame, "username: ", 0, 0, HEIGHT)
    guiUtilityFuncs.entranceLabelDesign(frame, "password: ", 1, 0, HEIGHT)

    #Inputs
    username = guiUtilityFuncs.entranceDesign(frame, 0, 1, HEIGHT)
    password = guiUtilityFuncs.entranceDesign(frame, 1, 1, HEIGHT)

    submitButton = Button(frame, text = "Log In", command = check, font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    submitButton.grid(row = 2, column = 0)

    goBack = Button(frame, text = "go back", command = lambda : guiUtilityFuncs.back(packs, root), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    goBack.grid(row = 3, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = guiUtilityFuncs.basicStructure(612, 378, 1, "Log In")
    main(root, 612, 378, 612/1000, 378/1000)

