from tkinter import *
import passChange

def change():
    global resultMessage
    result = passChange.passChange(username.get(), oldPassword.get(), newPassword.get())
    try:resultMessage.grid_forget()
    except Exception:pass
    if result.accepted:resultMessage = Label(frame, text = "password changed")
    else:resultMessage = Label(frame, text = result.message)
    resultMessage.grid(row = 5, column = 1)


def go_back():
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

    username_label = Label(frame, text = space_from_start + "username: ", font = "Roboto 15", pady = 10)
    username_label.grid(row = 0, column = 0)

    oldPassword_label = Label(frame, text = space_from_start + "old password: ", font = "Roboto 15", pady = 10)
    oldPassword_label.grid(row = 1, column = 0)

    newPassword_label = Label(frame, text = space_from_start + "new password: ", font = "Roboto 15", pady = 10)
    newPassword_label.grid(row = 2, column = 0)


    username = StringVar()
    oldPassword = StringVar()
    newPassword = StringVar()
    username_entry = Entry(frame, textvariable = username)
    oldPassword_entry = Entry(frame, textvariable = oldPassword)
    newPassword_entry = Entry(frame, textvariable = newPassword)


    username_entry.grid(row = 0, column = 1)
    oldPassword_entry.grid(row = 1, column = 1)
    newPassword_entry.grid(row = 2, column = 1)

    submit_button = Button(frame, text = "submit", command = change)
    submit_button.grid(row = 3, column = 0)

    goBack = Button(frame, text = "go back", command = go_back)
    goBack.grid(row = 4, column = 0)


    root.mainloop()