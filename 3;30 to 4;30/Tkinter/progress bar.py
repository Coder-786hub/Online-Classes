from tkinter import *
from tkinter  import ttk
root=Tk()

root.title("TikTok")
root.iconbitmap("icon.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)

progress=ttk.Progressbar(root,orient="vertical",length=100,mode="determinate")

def bar():
    import time
    progress["value"]=10
    root.update_idletasks()
    time.sleep(0.5)


    progress["value"]=20
    root.update_idletasks()
    time.sleep(0.5)

    progress["value"]=40
    root.update_idletasks()
    time.sleep(0.5)

    progress["value"]=60
    root.update_idletasks()
    time.sleep(0.5)

    progress["value"]=100
    root.update_idletasks()
    time.sleep(0.5)

    progress["value"]=80
    root.update_idletasks()
    time.sleep(0.5)

    progress["value"]=60
    root.update_idletasks()
    time.sleep(0.5)

    progress["value"]=40
    root.update_idletasks()
    time.sleep(0.5)

    progress["value"]=20
    root.update_idletasks()
    time.sleep(0.5)
    progress["value"]=0

progress.pack(pady=10)

btn=Button(root,text="start",command=bar)
btn.pack()
root.mainloop()