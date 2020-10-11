#imports
from tkinter import Tk, Frame, Button, SUNKEN, Y
import loginGui
import signUpGui
import passChangeGui
import deleteAccountGui

def login():
    #forget everything
    ClearRoot()

    #use the loginGui.py file
    try:
        loginGui.main(root);final(root)
    except Exception:pass


def signUp():
    #forget everything
    ClearRoot()

    #use the signUpGui.py file
    try:
        signUpGui.main(root);final(root)
    except Exception:pass


def deleteAccount():
    #forget everything
    ClearRoot()

    #use the DeleteAccountGui.py file
    try:
        deleteAccountGui.main(root);final(root)
    except Exception:pass


def passChange():
    #forget everything
    ClearRoot()

    #use the PassChangeGui.py file
    try:
        passChangeGui.main(root);final(root)
    except Exception:pass



def final(root):
    #Resetting basic settings.
    HEIGHT = 378
    WIDTH = 612
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.maxsize(WIDTH + 1, HEIGHT + 1)
    root.minsize(WIDTH - 1, HEIGHT - 1)
    root.title("Account Setup")

    #Login frame
    global f1
    f1 = Frame(root, bg = "red", padx = "25", pady = "50")
    f1.grid(row = 0, column = 0)
    login_in_button = Button(f1, text = "Log In", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = login)
    login_in_button.pack(fill = Y)

    #Delete account frame
    global f2
    f2 = Frame(root, bg = "red", padx = "25", pady = "50")
    f2.grid(row = 0, column = 1)
    sign_up_button = Button(f2, text = "Delete Account", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = deleteAccount)
    sign_up_button.pack()

    #Change password frame
    global f3
    f3 = Frame(root, bg = "red", padx = "25", pady = "50")
    f3.grid(row = 1, column = 0)
    changePass_button = Button(f3, text = "Change Password", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = passChange)
    changePass_button.pack()

    #Sign up frame
    global f4
    f4 = Frame(root, bg = "red", padx = "25", pady = "50")
    f4.grid(row = 1, column = 1)
    sign_up_button = Button(f4, text = "Sign Up", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = signUp)
    sign_up_button.pack()

    root.mainloop()

def ClearRoot():
    f1.grid_forget()
    f2.grid_forget()
    f3.grid_forget()
    f4.grid_forget()

if __name__ == "__main__":
    root = Tk()
    final(root)