from tkinter import *
root = Tk()

e = Entry(root,width=50,bg="yellow",borderwidth=5) #EntryWidget
e.pack()

e.insert(0,"Enter your name")
def myClick():
    hello = "Hello  "+e.get() + "  !!"
    myLabel = Label(root,text=hello)
    myLabel.pack()

myButton = Button(root , text = "Enter Your Name",padx = 50,pady=10,command=myClick,fg="red",bg="light green")# state = DISABLED)#don't put brackets in command
myButton.pack()

root.mainloop()
#When the window is closed, the mainloop ends, and the prog. ends