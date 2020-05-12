from tkinter import *

#everything in tkinter is a widget

root = Tk()

#Creating a LabelWidget
myLabel = Label(root , text="Hello World!!").grid(row = 0 , column = 0) #LabelWidget
myLabel2 = Label(root , text="Hello!!").grid(row = 1 , column = 1)
#Shoving it onto screen
#Other option
#myLabel.grid(row = 0 , column = 0)
#myLabel2.grid(row = 1 , column = 1)
root.mainloop()
#When the window is closed, the mainloop ends, and the prog. ends