from tkinter import *

app = Tk()
app.title("First GUI")
app.geometry("700x400")
app.config(background = "#99E5A7")

label = Label(app, text = "First GUI", font = ("ROBOT", 35, "bold"), background = "green", foreground = "white")
label.pack(fill = "x", ipady = 5)

name = Label(app, text = "User_name", font = ("ROBOT", 18, "bold"), background = "blue", foreground = "white")
name.place(x = 200, y = 100)

name = Label(app, text = "Password", font = ("ROBOT", 18, "bold"), background = "red", foreground = "white")
name.place(x = 200, y = 150)


entry1 = Entry(app, font =("arial", 18, "bold"), background = "lightgray")
entry1.place(x = 350, y = 100)

entry1 = Entry(app, font =("arial", 18, "bold"), background = "lightgray")
entry1.place(x = 350, y = 150)


btn = Button(app, text = "Submit",font = ("ROBOT", 18, "bold"), background = "green", foreground = "white", cursor = "hand2")
btn.place(x = 300, y = 230)
app.mainloop()