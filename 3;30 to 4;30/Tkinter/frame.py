from tkinter import *

# ========================================================Label Frame=============================================

root = Tk()
root.geometry("700x400")
root.title("Frame")
root.config(bg = "green")

f1 = LabelFrame(root, text = "Deatils", width = 300, height = 150, font = "arial 20 bold", fg = "red")
f1.place(x = 30, y = 20)

f1 = LabelFrame(root, text = "Conatct No", width = 300, height = 150, font = "arial 20 bold", fg = "green")
f1.place(x = 350, y = 20)

f1 = LabelFrame(root, text = "All Buttons", width = 600, height = 150, font = "arial 20 bold", fg = "red")
f1.place(x = 30, y = 200)

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