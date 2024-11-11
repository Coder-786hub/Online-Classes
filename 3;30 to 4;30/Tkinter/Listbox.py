from tkinter import *
from tkinter  import ttk
from  tkinter import messagebox
root=Tk()

root.title("TikTok")
# root.iconbitmap("tiktok.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)

def fun():
    lst.delete(ANCHOR)

lst=Listbox(root,width=15)
a=["apple", "banana","cherry"]
for i in a:
    lst.insert(END,i)
lst.pack()


btn=Button(root,text="Delete Item",command=fun)
btn.pack()
root.mainloop()