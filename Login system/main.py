#imports
from tkinter import *
import loginGui
import signUpGui
import passChangeGui
import deleteAccountGui

def login():
    #forget everything
    f1.grid_forget()
    f2.grid_forget()
    f3.grid_forget()
    f4.grid_forget()

    #use the Login_gui.py file
    try:
        loginGui.main(root)
        final(root)
    except Exception:pass

def sign_up():
    #forget everything
    f1.grid_forget()
    f2.grid_forget()
    f3.grid_forget()
    f4.grid_forget()

    #use the sign_up_gui.py file
    try:
        signUpGui.main(root)
        final(root)
    except Exception:pass

def deleteAccount():
    #forget everything
    f1.grid_forget()
    f2.grid_forget()
    f3.grid_forget()
    f4.grid_forget()

    #use the DeleteAccountGui.py file
    try:
        deleteAccountGui.main(root)
        final(root)
    except Exception:pass

def pass_change():
    f1.grid_forget()
    f2.grid_forget()
    f3.grid_forget()
    f4.grid_forget()

    #use the PassChangeGui.py file
    try:
        passChangeGui.main(root)
        final(root)
    except Exception:pass

    
#main structure
root = Tk()
root.geometry("612x378")
root.maxsize(612, 400)
root.title("Account setup")

def final(root):
    #resetting basic settings
    root.geometry("612x378")
    root.maxsize(612, 400)
    root.title("Account setup")

    #login in frame
    global f1
    f1 = Frame(root, bg = "red", padx = "25", pady = "50")
    f1.grid(row = 0, column = 0)
    login_in_button = Button(f1, text = "login in", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = login)
    login_in_button.pack(fill = Y)

    #delete account frame
    global f2
    f2 = Frame(root, bg = "red", padx = "25", pady = "50")
    f2.grid(row = 0, column = 1)
    sign_up_button = Button(f2, text = "delete Account", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = deleteAccount)
    sign_up_button.pack()


    #change password frame
    global f3
    f3 = Frame(root, bg = "red", padx = "25", pady = "50")
    f3.grid(row = 1, column = 0)
    changePass_button = Button(f3, text = "Change Password", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = pass_change)
    changePass_button.pack()

    #sign up frame
    global f4
    f4 = Frame(root, bg = "red", padx = "25", pady = "50")
    f4.grid(row = 1, column = 1)
    sign_up_button = Button(f4, text = "sign up", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = sign_up)
    sign_up_button.pack()


    root.mainloop()

if __name__ == "__main__":
    final(root)