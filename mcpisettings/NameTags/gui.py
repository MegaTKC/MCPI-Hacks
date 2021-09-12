import Tkinter
import tkMessageBox
import os
import sys

root = Tkinter.Tk()

root.title("NameTags")
root.geometry('350x200')

def enable():
    print "Enabled"
    os.system('python2 mcpisettings/NameTags/nametag-enable.py')

B = Tkinter.Button(root, text ="Enable", command = enable)

B.pack()

def disable():
    print "Disabled"
    os.system('python2 mcpisettings/NameTags/nametag-disable.py')

B = Tkinter.Button(root, text ="Disable", command = disable)

B.pack()

def quit():
    print "Quit NameTags Gui"
    root.destroy()

B = Tkinter.Button(root, text ="Quit", command = quit)

B.pack()
root.mainloop()
