from tkinter import *
from tkinter  import ttk
root=Tk()

root.title("TikTok")
# root.iconbitmap("tiktok.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)


def fun():
    top.destroy()

def fun1():
    root.destroy()

top=Toplevel()


btn=Button(top,text= "Close Window",command =fun)
btn.pack()

btn1=Button(root,text="Close Window",command=fun1)
btn1.pack()

root.mainloop()