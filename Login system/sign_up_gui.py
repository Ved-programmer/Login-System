from tkinter import *
import signup

def go_back():
    global global_root
    for i in packs:
        i.pack_forget()
    
    #remaking initial setup
    global_root.quit()

def check():
    global sign_up_message
    result = signup.addToIndex(username.get(), password.get())
    try:sign_up_message.grid_forget()
    except Exception:pass
    if result.accepted:sign_up_message = Label(frame, text = "created account")
    else:sign_up_message = Label(frame, text = result.message)
    sign_up_message.grid(row = 2, column = 1)

def main(root):
    global frame
    global username
    global password
    global packs
    global global_root
    global_root = root
    root.title("sign up")
    packs = []

    heading = Label(text = "sign up", bg="black", fg = "yellow", padx = "50", pady = "30", font = "OpenSans 30 ")
    packs.append(heading)
    heading.pack(fill = X, side = TOP, pady = 5)

    frame = Frame(root)
    packs.append(frame)
    frame.pack(side = LEFT, anchor = "nw")
    space_from_start = " " * 3

    username_label = Label(frame, text = space_from_start + "username: ", font = "Roboto 15", pady = 10)
    username_label.grid(row = 0, column = 0)

    password_label = Label(frame, text = space_from_start + "password: ", font = "Roboto 15", pady = 10)
    password_label.grid(row = 1, column = 0)

    username = StringVar()
    password = StringVar()
    username_entry = Entry(frame, textvariable = username)
    password_entry = Entry(frame, textvariable = password)

    username_entry.grid(row = 0, column = 1)
    password_entry.grid(row = 1, column = 1)

    submit_button = Button(frame, text = "submit", command = check)
    submit_button.grid(row = 2, column = 0)

    goBack = Button(frame, text = "go back", command = go_back)
    goBack.grid(row = 3, column = 0)

    root.mainloop()