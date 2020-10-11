from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import passChange

def change():
    global resultMessage
    result = passChange.passChange(username.get(), oldPassword.get(), newPassword.get())
    try:resultMessage.grid_forget()
    except Exception:pass
    if result.accepted:resultMessage = Label(frame, text = "password changed")
    else:resultMessage = Label(frame, text = result.message)
    resultMessage.grid(row = 5, column = 1)


def back():
    global globalRoot
    for i in packs:
        i.pack_forget()
    
    #remaking initial setup
    globalRoot.quit()

def main(root):
    global globalRoot
    global packs
    global username
    global oldPassword
    global newPassword
    global frame
    
    root.title("Change Password")
    globalRoot = root
    packs = []

    heading = Label(text = "Change Password", bg="black", fg = "yellow", padx = "50", pady = "30", font = "OpenSans 30 ")
    packs.append(heading)
    heading.pack(fill = X, side = TOP, pady = 5)

    frame = Frame(root)
    packs.append(frame)
    frame.pack(side = LEFT, anchor = "nw")
    space_from_start = " " * 3

    usernameLabel = Label(frame, text = space_from_start + "username: ", font = "Roboto 15", pady = 10)
    usernameLabel.grid(row = 0, column = 0)

    oldPasswordLabel = Label(frame, text = space_from_start + "old password: ", font = "Roboto 15", pady = 10)
    oldPasswordLabel.grid(row = 1, column = 0)

    newPasswordLabel = Label(frame, text = space_from_start + "new password: ", font = "Roboto 15", pady = 10)
    newPasswordLabel.grid(row = 2, column = 0)


    username = StringVar()
    oldPassword = StringVar()
    newPassword = StringVar()
    usernameEntry = Entry(frame, textvariable = username)
    oldPasswordEntry = Entry(frame, textvariable = oldPassword)
    newPasswordEntry = Entry(frame, textvariable = newPassword)


    usernameEntry.grid(row = 0, column = 1)
    oldPasswordEntry.grid(row = 1, column = 1)
    newPasswordEntry.grid(row = 2, column = 1)

    submitButton = Button(frame, text = "submit", command = change)
    submitButton.grid(row = 3, column = 0)

    goBack = Button(frame, text = "go back", command = back)
    goBack.grid(row = 4, column = 0)


    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    HEIGHT = 378
    WIDTH = 612
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.maxsize(WIDTH + 1, HEIGHT + 1)
    root.minsize(WIDTH - 1, HEIGHT - 1)
    main(root)
