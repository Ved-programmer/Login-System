from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import login
def back():
    global globalRoot

    #forgetting everything
    for i in packs:
        i.pack_forget()
    
    #remaking initial setup
    globalRoot.quit()

def check():
    global loginMessage

    try:loginMessage.grid_forget()
    except Exception:pass

    if login.login_or_not(username.get(), password.get()):
        loginMessage = Label(frame, text = "you are now logged in")
    else:
        loginMessage = Label(frame, text = "incorrect username or password")

    loginMessage.grid(row = 2, column = 1)

def main(root):
    global frame
    global username
    global password
    global packs
    global globalRoot
    globalRoot = root
    root.title("Log In")
    packs = []

    heading = Label(text = "Log In", bg="black", fg = "yellow", padx = "50", pady = "30", font = "OpenSans 30 ")
    packs.append(heading)
    heading.pack(fill = X, side = TOP, pady = 5)

    frame = Frame(root)
    packs.append(frame)
    frame.pack(side = LEFT, anchor = "nw")
    space_from_start = " " * 3

    usernameLabel = Label(frame, text = space_from_start + "username: ", font = "Roboto 15", pady = 10)
    usernameLabel.grid(row = 0, column = 0)

    passwordLabel = Label(frame, text = space_from_start + "password: ", font = "Roboto 15", pady = 10)
    passwordLabel.grid(row = 1, column = 0)

    username = StringVar()
    password = StringVar()
    usernameEntry = Entry(frame, textvariable = username)
    passwordEntry = Entry(frame, textvariable = password)

    usernameEntry.grid(row = 0, column = 1)
    passwordEntry.grid(row = 1, column = 1)

    submitButton = Button(frame, text = "submit", command = check)
    submitButton.grid(row = 2, column = 0)

    goBack = Button(frame, text = "go back", command = back)
    goBack.grid(row = 3, column = 0)

    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    HEIGHT = 378
    WIDTH = 612
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.maxsize(WIDTH + 1, HEIGHT + 1)
    root.minsize(WIDTH - 1, HEIGHT - 1)
    main(root)
