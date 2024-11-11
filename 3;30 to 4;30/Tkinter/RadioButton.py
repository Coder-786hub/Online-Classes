from tkinter import *
from tkinter  import ttk
root=Tk()

root.title("TikTok")
root.iconbitmap("icon.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)
 
def fun():
    if var.get()==0:
        print("Male")
    else:
        print("Female")

var= IntVar()

radio=Radiobutton(root,text="Male",value=0,variable=var)
radio.pack()

radio=Radiobutton(root,text="Female",value=1,variable=var)
radio.pack()

#button

btn=Button(root,text="Submit",command=fun)
btn.pack()

root.mainloop()