#imports
from tkinter import Tk, Frame, Button, SUNKEN, Y
import loginGui, signUpGui, passChangeGui, deleteAccountGui, showAbout

#Switching File, given the fileName
def switchFile(file):
    def main():
        ClearRoot()
        try:
            file.main(root)
            final(root)
        except Exception:pass
    return main

def final(root):
    #Setting basic settings.
    HEIGHT = 502
    WIDTH = 612
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.maxsize(WIDTH, HEIGHT); root.minsize(WIDTH, HEIGHT)
    root.title("Account Setup")

    global loginFrame, deleteAccountFrame, changePasswordFrame, signUpFrame, packs
    packs = []

    #Login frame
    loginFrame = makeFrame(root, 0, 0)
    makeButton(loginFrame, "Log In", switchFile(loginGui))

    #Delete account frame
    deleteAccountFrame = makeFrame(root, 0, 1)
    makeButton(deleteAccountFrame, "Delete Account", switchFile(deleteAccountGui))

    #Change password frame
    changePasswordFrame = makeFrame(root, 1, 0)
    makeButton(changePasswordFrame, "Change Password", switchFile(passChangeGui))

    #Sign up frame
    signUpFrame = makeFrame(root, 1, 1)
    makeButton(signUpFrame, "Sign up", switchFile(signUpGui))

    aboutMeFrame = Frame(root, bg = "red", padx = "67", pady = "13")
    button = Button(aboutMeFrame, text = "About me", bg="black", fg = "yellow", height = "2", width = "34", font = "comicsansms 17", borderwidth = 15, relief = SUNKEN, command = switchFile(showAbout))
    button.pack()
    aboutMeFrame.grid(row = 2, column = 0, columnspan = 2)
    packs.append(aboutMeFrame)

    root.mainloop()

#Emptying everything packed
def ClearRoot():
    for i in packs:i.grid_forget()

#Button Design
def makeButton(Master, Text, Function):
    button = Button(Master, text = Text, bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = Function)
    button.pack()
    return button

#Frame Design
def makeFrame(Master, Row, Col):
    frame = Frame(Master, bg = "red", padx = "25", pady = "50")
    frame.grid(row = Row, column = Col)
    packs.append(frame)
    return frame

#Execution
if __name__ == "__main__":
    root = Tk()
    final(root)
