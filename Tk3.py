from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root,text="LOOK !!")
    myLabel.pack()

myButton = Button(root , text = "Click Me!!",padx = 50,pady=10,command=myClick,fg="red",bg="light green")# state = DISABLED)#don't put brackets in command
myButton.pack()

root.mainloop()
#When the window is closed, the mainloop ends, and the prog. ends