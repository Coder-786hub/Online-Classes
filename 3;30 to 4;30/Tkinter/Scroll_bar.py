from tkinter import *
from tkinter  import ttk
root=Tk()

root.title("TikTok")
root.iconbitmap("icon.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)

scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)

# my_list=Text(root,yscrollcommand=Y)
my_list=Listbox(root,yscrollcommand=Y)
for i in range(100):
    my_list.insert(END,i)

my_list.pack(side=LEFT, fill=Y)
scroll.config(command=my_list.yview)


root.mainloop()