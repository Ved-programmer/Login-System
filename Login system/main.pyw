#imports
from tkinter import Tk, Frame, Button, SUNKEN, Y
import loginGui, signUpGui, passChangeGui, deleteAccountGui, showAbout
from win32api import GetSystemMetrics
import ctypes
import tkinter.font as tkFont

#Switching File, given the fileName
def switchFile(file):
    def main():
        deleteMe = clearRoot()
        try:
            file.main(root, WIDTH, HEIGHT, wu, hu)
            deleteMe.place_forget()
            final(root)
        except Exception:pass
    return main

def final(root):

    global WIDTH, HEIGHT, wu, hu
    
    # Increasing the DPI settings
    awareness = ctypes.c_int()
    ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
    ctypes.windll.shcore.SetProcessDpiAwareness(2)

    WIDTH, HEIGHT = GetSystemMetrics(0)//2, GetSystemMetrics(1)//2 # Original
    # WIDTH, HEIGHT = GetSystemMetrics(0)//3, GetSystemMetrics(1)//3
    # WIDTH, HEIGHT = GetSystemMetrics(0)*3//4, GetSystemMetrics(1)*3//4
    wu = WIDTH/1000
    hu = HEIGHT/1000

    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.maxsize(WIDTH, HEIGHT); root.minsize(WIDTH, HEIGHT)
    root.title("Account Setup")
    root.config(bg = "red")

    with open("data.txt", "a"):
        pass

    buttonWidth, buttonHeight = wu*450, hu*250
    marginX, marginY = 30*wu, 50*hu

    containerSize = 350*hu
    CONTROL_Y = HEIGHT - containerSize
    marginalSpace = (containerSize - buttonHeight)/2

    startX = marginX
    endX = WIDTH - marginX - buttonWidth
    startY = marginY
    endY = CONTROL_Y - marginY - buttonHeight
    
    makeButton(root, "Log In", switchFile(loginGui), buttonWidth, buttonHeight, startX, startY)
    makeButton(root, "Delete Account", switchFile(deleteAccountGui), buttonWidth, buttonHeight, startX, endY)
    makeButton(root, "Change Password", switchFile(passChangeGui), buttonWidth, buttonHeight, endX, endY)
    makeButton(root, "Sign up", switchFile(signUpGui), buttonWidth, buttonHeight, endX, startY)

    makeButton(root, "About Me", switchFile(showAbout), WIDTH - 2 * marginX, buttonHeight, startX, CONTROL_Y + marginalSpace)

    root.mainloop()

#Button Design
def makeButton(root, Text, Function, width, height, xPos, yPos):
    font = tkFont.Font(size = -int(height/3))
    button = Button(root, text = Text, bg="black", fg = "yellow",
            font = font, borderwidth = 15, relief = SUNKEN, command = Function)
    button.place(x = xPos, y = yPos, width = width, height = height)

def clearRoot():
    frame = Frame(root, bg = "white")
    frame.place(x = 0,  y = 0, width = WIDTH, height = HEIGHT)
    return frame

    
#Execution
if __name__ == "__main__":
    root = Tk()
    final(root)
