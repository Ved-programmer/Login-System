from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import tkinter.font as tkFont
import utility
import hashing

def delete(username, password):
    if utility.checkIfCorrect(username, password):
        with open("data.txt", "r") as f:
            lines = f.readlines()
        try:lines.remove(f"{username}-{hashing.encrypt(password)}\n")
        except Exception:lines.remove(f"{username}-{hashing.encrypt(password)}")
        with open("data.txt", "w") as f:
            for i in lines:
                f.write(i)
        return True
    return False

#Deleting Logic
def deletionWithGui():
    global deleteMessage
    result = delete(username.get(), password.get())
    try:deleteMessage.grid_forget()
    except Exception:pass
    if result:deleteMessage = Label(frame, text = "Deleted Account", font = messageHeight)
    else:deleteMessage = Label(frame, text = "Incorrect Username or Password", font = messageHeight)
    deleteMessage.grid(row = 2, column = 1)

def main(root, WIDTH, HEIGHT, wu, hu):
    #Initialization
    global frame, username, password, packs
    global messageHeight
    messageHeight = tkFont.Font(size = -int(HEIGHT/20))

    root.title("Delete Account")
    packs = []

    #Heading and setting Frame
    utility.headingDesign("Delete Account", packs, root, HEIGHT)
    frame = utility.formFrameDesign(root, packs, WIDTH)
    
    #Labels
    utility.entranceLabelDesign(frame, "username: ", 0, 0, HEIGHT)
    utility.entranceLabelDesign(frame, "password: ", 1, 0, HEIGHT)

    #Inputs
    username = utility.entranceDesign(frame, 0, 1, HEIGHT)
    password = utility.entranceDesign(frame, 1, 1, HEIGHT)

    submitButton = Button(frame, text = "Delete Account", command = deletionWithGui, font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    submitButton.grid(row = 2, column = 0)
    
    goBack = Button(frame, text = "Go back", command = lambda : utility.back(packs, root), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    goBack.grid(row = 3, column = 0)

    root.mainloop()
    

if __name__ == "__main__":
    root = utility.basicStructure(612, 378, 1, "Delete Account")
    main(root, 612, 378, 612/1000, 378/1000)

