import sys
import os
import time

import threading
from threadsafe_tkinter import *

count = 0
try:
    os.mkfifo("count")
except:
    pass  # In case one of your other files already started
    if True:
        file = open("count", "w")
        file.write(str(count))
        file.close()
# names = ["a","b","c"]
names = []
# data = ["1","2","3"]
data = []






root = Tk()

nameholder1 = StringVar()
nameholder2 = StringVar()
nameholder3 = StringVar()
nameholder4 = StringVar()
nameholder5 = StringVar()
countholder = StringVar()

def updatenames():
    if count > 4:
        nameholder5.set(names[4])
        nameholder4.set(names[3])
        nameholder3.set(names[2])
        nameholder2.set(names[1])
        nameholder1.set(names[0])
    elif count > 3:
        nameholder5.set("")
        nameholder4.set(names[3])
        nameholder3.set(names[2])
        nameholder2.set(names[1])
        nameholder1.set(names[0])
    elif count > 2:
        nameholder5.set("")
        nameholder4.set("")
        nameholder3.set(names[2])
        nameholder2.set(names[1])
        nameholder1.set(names[0])
    elif count > 1:
        nameholder5.set("")
        nameholder4.set("")
        nameholder3.set("")
        nameholder2.set(names[1])
        nameholder1.set(names[0])
    elif count > 0:
        nameholder5.set("")
        nameholder4.set("")
        nameholder3.set("")
        nameholder2.set("")
        nameholder1.set(names[0])
    else:
        nameholder5.set("")
        nameholder4.set("")
        nameholder3.set("")
        nameholder2.set("")
        nameholder1.set("")
        print("nothing to update")
    countholder.set("# of requests: " + str(count))


def deleteitem(num):
    global count
    if len(names) > (num):
        del names[num]
        del data[num]
        count = len(names)
        try:
            os.mkfifo("count")
        except:
            pass  # In case one of your other files already started
            if True:
                file = open("count", "w")
                file.write(str(count))
                file.close()
                print(data)
                print(names)
                updatenames()
    else:
        print("there is nothing stored there")


def updatedata():
    try:
        os.mkfifo("data.txt")
    except:
        pass  # In case one of your other files already started
        if True:
            file = open("data.txt", "r")
            newraw = file.read()
            file.close()
        rawdata = newraw.split("~")[0]
        newname = newraw.split("~")[1]

        names.append(newname + " " + (newraw.split(" ")[0].split("!")[1]))
        data.append(rawdata)
        updatenames()


def datacheck():
    global count
    threading.Timer(0.01, datacheck).start()
    try:
        os.mkfifo("count")
    except:
        pass  # In case one of your other files already started
    if True:
        file = open("count", "r")
        readcount = int(file.read())
        #print(readcount)
        if int(readcount) != int(count):
            print("new data")
            count = readcount
            updatedata()

def playnotes(num):
    unparsed = data[num]
    try:
        os.mkfifo("play")
    except:
        pass  # In case one of your other files already started
        if True:
            file = open("play", "r")
            status = file.read()
            file.close()
            print("status of player = " + status)
    if status == 1:
        print("midi sequencer is busy")
    else:
        try:
            os.mkfifo("play")
        except:
            pass  # In case one of your other files already started
            if True:
                file = open("play", "w")
                file.write("1")
                file.close()
                print("play set to 1")
        try:
            os.mkfifo("notes")
        except:
            pass  # In case one of your other files already started
            if True:
                file = open("notes", "w")
                file.write(unparsed)
                file.close()
                print("data: '" + unparsed + "' written")

def notecheck(num):
    if len(names) > (num):
        print("playing notes from " + str(num))
        playnotes(num)
    else:
        print("there is nothing stored there")


datacheck()


def playnotes1(event):
    notecheck(0)


def playnotes2(event):
    notecheck(1)


def playnotes3(event):
    notecheck(2)


def playnotes4(event):
    notecheck(3)


def playnotes5(event):
    notecheck(4)


def delete1(event):
    deleteitem(0)

def delete2(event):
    deleteitem(1)

def delete3(event):
    deleteitem(2)

def delete4(event):
    deleteitem(3)

def delete5(event):
    deleteitem(4)

root.title("KeysBot Queue")
root.configure(background='green')

lbl1 = Label(root, text="1")
lbl1.grid(column=0,row=0)

name1 = Label(root, textvariable=nameholder1)
name1.grid(column=1,row=0)

play1 = Button(root, text="play")
play1.bind("<Button-1>", playnotes1)
play1.grid(column=0,row=1)

del1 = Button(root, text="delete")
del1.bind("<Button-1>", delete1)
del1.grid(column=1,row=1)

lbl2 = Label(root, text="2")
lbl2.grid(column=0,row=2)

name2 = Label(root, textvariable=nameholder2)
name2.grid(column=1,row=2)

play2 = Button(root, text="play")
play2.bind("<Button-1>", playnotes2)
play2.grid(column=0,row=3)

del2 = Button(root, text="delete")
del2.bind("<Button-1>", delete2)
del2.grid(column=1,row=3)

lbl3 = Label(root, text="3")
lbl3.grid(column=0,row=4)

name3 = Label(root, textvariable=nameholder3)
name3.grid(column=1,row=4)

play3 = Button(root, text="play")
play3.bind("<Button-1>", playnotes3)
play3.grid(column=0,row=5)

del3 = Button(root, text="delete")
del3.bind("<Button-1>", delete3)
del3.grid(column=1,row=5)

lbl4 = Label(root, text="4")
lbl4.grid(column=0,row=6)

name4 = Label(root, textvariable=nameholder4)
name4.grid(column=1,row=6)

play4 = Button(root, text="play")
play4.bind("<Button-1>", playnotes4)
play4.grid(column=0,row=7)

del4 = Button(root, text="delete")
del4.bind("<Button-1>", delete4)
del4.grid(column=1,row=7)

lbl5 = Label(root, text="5")
lbl5.grid(column=0,row=8)

name5 = Label(root, textvariable=nameholder5)
name5.grid(column=1,row=8)

play5 = Button(root, text="play")
play5.bind("<Button-1>", playnotes5)
play5.grid(column=0,row=9)

del5 = Button(root, text="delete")
del5.bind("<Button-1>", delete5)
del5.grid(column=1,row=9)

totalrequests = Label(root, textvariable=countholder)
totalrequests.grid(column=0,row=10)
root.mainloop()
