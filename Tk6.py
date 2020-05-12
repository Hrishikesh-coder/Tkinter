from tkinter import *
from PIL import ImageTk,Image
root = Tk()

root.title("Hello , H.B. here!!")

#root.iconbitmap("")#Pass the location of the file(.ico file)

img1 = ImageTk.PhotoImage(Image.open("images/Ahmedabad Satyagraha.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/download.jfif"))
img3 = ImageTk.PhotoImage(Image.open("images/khilafat.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/khilaft_movement.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/ghandi-by-rajuarya[221559].jpg"))

image_list = [img1,img2,img3,img4,img5]



my_label = Label(image=img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward():
      return

def back():
      return

button_back = Button(root,text="<<",command=lambda : back())
button_exit = Button(root,text="EXIT PROGRAM",command=root.destroy)
button_forward = Button(root,text=">>",command=lambda:forward())

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()
