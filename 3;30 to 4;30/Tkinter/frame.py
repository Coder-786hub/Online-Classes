from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import  ttk

# ================================================LabelFrame===================================

def exit_():
    root.destroy()

def submit():
    input_ = e1.get()
    if input_== "":
        messagebox.showerror("Error", "Insert something")
    else:
        messagebox.showinfo("Success", "Data Submited")    


root = Tk()
root.geometry("700x400")
root.title("Frame")
# root.config(bg = "green")
root.iconbitmap("icon.ico")

image = Image.open("Jarvis.jpg")
image = image.resize((700, 400))
image = ImageTk.PhotoImage(image)

background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)





f1 = LabelFrame(root, text = "Deatils", width = 300, height = 150, font = "arial 20 bold", fg = "red")
f1.place(x = 30, y = 20)

l1 = Label(f1, text = "Name")
l1.place(x = 10, y = 10)

l2 = Label(f1, text = "Gender")
l2.place(x = 10, y = 40)

e1 = Entry(f1, bg = "red")
e1.place(x = 70, y = 10)

combo = ttk.Combobox(f1, textvariable = StringVar(), state = "readonly", values = ["Male", "Female"])
combo.current(0)
combo.place(x = 90, y = 40)



f2 = LabelFrame(root, text = "Conatct No", width = 300, height = 150, font = "arial 20 bold", fg = "green")
f2.place(x = 350, y = 20)

combo = Spinbox(f2, textvariable = StringVar(), state = "readonly", values = ["Male", "Female"])
# combo.current(0)
combo.place(x = 90, y = 40)
# number = Label(f2, text = "Contact No", )

f3 = LabelFrame(root, text = "All Buttons", width = 600, height = 150, font = "arial 20 bold", fg = "red")
f3.place(x = 30, y = 200)

btn = Button(f3, text = "SUBMIT", bg = "green", font = "arial 20 bold", bd = 4, relief = "groove", command = submit)
btn.place(x = 10, y = 10)

exit_btn = Button(f3, text = "EXIT", bg = "red", font = "arial 20 bold", bd = 4, command = exit)
exit_btn.place(x = 500, y = 10)

root.mainloop()
























# =================================================Frame=====================================================











# # Frame 1
# f1 = Frame(root,bg = "white", height = 150, width = 300)
# f1.place(x = 20, y = 20)

# l1 = Label(f1, text = "Name")
# l1.place(x = 10, y = 10)

# e1 = Entry(f1, bg = "green")
# e1.place(x = 70, y = 10)


# # Frame 2
# f2 = Frame(root, bg = "white", width = 300, height = 150)
# f2.place(x = 380, y = 20)

# l1 = Label(f2, text = "Father Name")
# l1.place(x = 10, y = 10)

# e1 = Entry(f2, bg = "green")
# e1.place(x = 120, y = 10)

# # btn Frame
# btn_frame = Frame(root, bg = "white", width = 500, height = 150)
# btn_frame.place(x = 100, y = 200)

# l1 = Label(btn_frame, text = "Mother Name")
# l1.place(x = 10, y = 10)

# e1 = Entry(btn_frame, bg = "green")
# e1.place(x = 100, y = 10)

# root.mainloop()