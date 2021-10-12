import hashing

from tkinter import Tk, Label, Frame, X, TOP, LEFT, StringVar, Entry
import tkinter.font as tkFont


# Back End

def usernameExists(username):
    with open("data.txt", "r") as f:
        for i in f.readlines():
            if i == "\n":continue
            if i[:i.index("-")] == username:return True
    
    return False

def getLine(username):
    if not usernameExists(username):return False
    index = 0
    with open("data.txt", "r") as f:
        cur = f.readline()
        while cur.split("-")[0] != username:
            cur = f.readline()
            index += 1
        return [index, cur.removesuffix("\n")]
    return [-1, ""]

def checkIfCorrect(username, password):
    line = getLine(username)
    if line == False:return False
    storePassword = line[1][line[1].index("-") + 1:]
    userPasswordHash = hashing.encrypt(password)
    return storePassword == userPasswordHash


# Front End

def back(packs, globalRoot):
    for i in packs:i.pack_forget()
    globalRoot.quit()

def headingDesign(Text, packs, root, HEIGHT):
    heading = Label(root, text = Text, bg="black", fg = "yellow", padx = "50", pady = "30", font = tkFont.Font(size = -int(HEIGHT/8)))
    packs.append(heading)
    heading.pack(fill = X, side = TOP, pady = 5)
    return heading

def formFrameDesign(root, packs, WIDTH):
    frame = Frame(root)
    packs.append(frame)
    frame.pack(fill = X)
    return frame

def entranceLabelDesign(master, Text, Row, Col, HEIGHT):
    space_from_start = " " * 3
    usernameLabel = Label(master, text = space_from_start + Text, font = tkFont.Font(size = -int(HEIGHT/10)), pady = 10)
    usernameLabel.grid(row = Row, column = Col)
    return usernameLabel

def entranceDesign(master, Row, Col, HEIGHT, typeVar = StringVar):
    entranceVar = typeVar()
    entranceEntry = Entry(master, textvariable = entranceVar, font = tkFont.Font(size = -int(HEIGHT/20)))
    entranceEntry.grid(row = Row, column = Col)
    return entranceVar

def basicStructure(width = 612, height = 378, difference = 1, Title = "Tk"):
    root = Tk()
    root.geometry(f"{width}x{height}")
    root.title(Title)
    root.minsize(width - difference, height - difference)
    root.maxsize(width + difference, height + difference)
    return root

