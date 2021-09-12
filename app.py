# MCPI Hacks GUI Panel / Requires Python 3

import Tkinter
import tkMessageBox
import os
import sys

root = Tkinter.Tk()

root.title("MCPI Enhancer")
root.geometry('350x200')

# Hacks / Modules Start
def chatSpammer():
    print "chat-spammer.py running"
    os.system('python2 chat-spammer.py')

B = Tkinter.Button(root, text ="ChatSpammer", command = chatSpammer)

B.pack()

def scaffoldWalk():
    print "scaffold.py running"
    os.system('python2 scaffold.py')

B = Tkinter.Button(root, text ="Scaffold", command = scaffoldWalk)

B.pack()

def nametags():
    print "nametagsGui running"
    os.system('python2 mcpisettings/NameTags/gui.py')

B = Tkinter.Button(root, text ="NameTags", command = nametags)

B.pack()

def autojump():
    print "autojumpGui running"
    os.system('python2 mcpisettings/AutoJump/gui.py')

B = Tkinter.Button(root, text ="AutoJump", command = autojump)

B.pack()

def quit():
    print "Good Bye!"
    root.destroy()

B = Tkinter.Button(root, text ="Quit", command = quit)

B.pack()
root.mainloop()
