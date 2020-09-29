#imports
from tkinter import *
from PIL import Image, ImageTk
import login_gui
import sign_up_gui

def login():
    #forget everything
    f1.pack_forget()
    f2.pack_forget()
    ved_photo.pack_forget()

    #use the Login_gui.py file
    try:
        login_gui.main(root)
        final(root)
    except Exception:pass

def sign_up():
    #forget everything
    f1.pack_forget()
    f2.pack_forget()
    ved_photo.pack_forget()

    #use the sign_up_gui.py file
    try:
        sign_up_gui.main(root)
        final(root)
    except Exception:pass
    
#main structure
root = Tk()
root.geometry("610x462")
root.maxsize(612, 463)
root.title("Account setup")

def final(root):

    #login in frame
    global f1
    f1 = Frame(root, bg = "red", padx = "10")
    f1.pack(fill = Y, side = LEFT)
    login_in_button = Button(f1, text = "login in", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = login)
    login_in_button.pack(fill = Y, pady = 10)

    #sign up frame
    global f2
    f2 = Frame(root, bg = "red", pady = 30)
    f2.pack(side = BOTTOM, fill = X)
    sign_up_button = Button(f2, text = "sign up", bg="black", fg = "yellow", height = "2", width = "20", font = "comicsansms 15", borderwidth = 15, relief = SUNKEN, command = sign_up)
    sign_up_button.pack()

    #packing the photo
    global ved_photo
    photo = Image.open("ved.jpg")
    image = photo.resize((335, 310), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    ved_photo = Label(image = photo)
    ved_photo.pack(side = RIGHT, anchor = "ne")

    root.mainloop()

if __name__ == "__main__":
    final(root)