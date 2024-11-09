from tkinter import *
from tkinter  import ttk
from tkinter import messagebox
root=Tk()

root.title("TikTok")
root.iconbitmap("tiktok.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)

def fun():
    if var.get()=="":
        messagebox.showerror("Warning ","Please enter a valid username.")
    else:
        messagebox.showinfo("Success","Username is available!")
var=StringVar()
ent=Entry(root,textvariable=var)
ent.pack()

btn=Button(root,text="Submit",command=fun)
btn.pack()

root.mainloop()



# showinfo()
# showwarning()
# showerror()
# askquestion()
# askokcancel()
# askyesno()
# askretrycancel()