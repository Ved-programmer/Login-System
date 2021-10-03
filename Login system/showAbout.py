from tkinter import *
import webbrowser
import tkinter.font as tkFont

def main(root, WIDTH, HEIGHT, wu, hu):
    win = Frame(root, bg = "black")
    win.place(x = 0, y = 0, width = WIDTH, height = HEIGHT)

    
    
    Label(win, text = "About The creators", font = tkFont.Font(size = -int(HEIGHT/8)), fg = "white", bg = "black").place(x = WIDTH//2, y = 100*hu, anchor = "center")

    string = """
    The first version of the project was created by 
    Navdeep Kante, assisted by Ved Rathi. 
    """

    def back():
        win.place_forget()
        root.quit()

    Label(win, text = string, font = tkFont.Font(size = -int(HEIGHT/13)), justify = "left").place(x = WIDTH//2, y = HEIGHT//2, anchor = "center")

    Button(win, text = "Go Back", font = tkFont.Font(size = -int(HEIGHT/15)), justify = "center", bg = "red", command = back).place(x = 0, y = 0)

    yPos = 700*hu
    width = 400*wu
    margin = 75*wu

    Button(win, text = "Ved's Github", font = tkFont.Font(size = -int(HEIGHT/13)), justify = "center", bg = "red", command = lambda : webbrowser.open("https://github.com/Ved-programmer")).place(x = margin, y = yPos, width = width)
    Button(win, text = "Navdeep's Github", font = tkFont.Font(size = -int(HEIGHT/13)), justify = "center", bg = "red", command = lambda : webbrowser.open("https://github.com/crypto-navdeep")).place(x = WIDTH - margin - width, y = yPos, width = width)

    root.mainloop()

