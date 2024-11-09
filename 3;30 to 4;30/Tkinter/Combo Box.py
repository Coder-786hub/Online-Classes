from tkinter import *
from tkinter  import ttk
root=Tk()

root.title("TikTok")
root.iconbitmap("icon.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)

var= StringVar()

con=ttk.Combobox(root,width=10,textvariable=var)
con['state']="readonly"
con["values"] = ("Jan","feb","Mar","Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
con.place(x=10,y=10)
con.current(8)


root.mainloop()