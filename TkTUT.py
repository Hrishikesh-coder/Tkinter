from tkinter import *

#everything in tkinter is a widget

root = Tk()

#Creating a LabelWidget
myLabel = Label(root , text="Hello World!!") #LabelWidget

#Shoving it onto screen
myLabel.pack()

root.mainloop()
#When the window is closed, the mainloop ends, and the prog. ends