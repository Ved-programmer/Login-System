from tkinter import *
import webbrowser
def main(root):
    HEIGHT = 502
    WIDTH = 612

    win = Frame(root, bg = "black")
    win.place(x = 0, y = 0, width = WIDTH, height = HEIGHT)

    Label(win, text = "About The creators", font = (" ", int(30)), fg = "white", bg = "black").place(x = WIDTH//2, y = 100, anchor = "center")

    string = """
    The first version of the project was created by 
    Navdeep Kante, assisted by Ved Rathi. 
    """

    def back():
        win.place_forget()
        root.quit()

    Label(win, text = string, font = (" ", int(15)), justify = "left").place(x = WIDTH//2, y = HEIGHT//2, anchor = "center")

    Button(win, text = "Go Back", font = (" ", int(15)), justify = "center", bg = "red", command = back).place(x = 0, y = 0)
    Button(win, text = "Ved's Github", font = (" ", int(15)), justify = "center", bg = "red", command = lambda : webbrowser.open("https://github.com/Ved-programmer")).place(x = 50, y = 400, width = 250)
    Button(win, text = "Navdeep's Github", font = (" ", int(15)), justify = "center", bg = "red", command = lambda : webbrowser.open("https://github.com/smartnavdeep")).place(x = 312, y = 400, width = 250)

    root.mainloop()

