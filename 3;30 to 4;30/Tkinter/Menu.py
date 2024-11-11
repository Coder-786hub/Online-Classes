

# Menus in Tkinter (GUI Programming)
# The tkinter menu is a top-level pulldown menu. They are shown just under the title bar, as you’d expect from traditional gui apps.

# The menu can have multiple sub menus and each sub menu can contain items. Menu items can be associated with callback methods, meaning when you click them a Python method is called.

"""Adding a menu is very straightforward, but it can be a bit confusing if it’s the first time you’re doing it. First create the top menu with these lines:"""

# self.master = master
# menu = Menu(self.master)
# self.master.config(menu=menu)
# Then you can add menus to this menu:

# fileMenu = Menu(menu)
# menu.add_cascade(label="File", menu=fileMenu)

# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# Each of those sub menus can have items:

# fileMenu.add_command(label="Item")
# fileMenu.add_command(label="Exit", command=self.exitProgram)
# editMenu.add_command(label="Undo")
# editMenu.add_command(label="Redo")

# Menu items can be clickable, you can specify the callback method in the same way as buttons (command=). The click will then call a Python method.


# tkinter menu example
# The menu example below adds a menu to a basic tkinter window. It has one clickable menu item but shows a complete menu.

from tkinter import *
from tkinter import ttk

root = Tk()

root.title("TikTok")
root.iconbitmap("icon.ico")
root.maxsize(width=500, height=360)
root.minsize(width=480, height=270)

def demo():
    pass

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=demo)
file_menu.add_command(label="Open", command=demo)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo", command=demo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=demo)
edit_menu.add_command(label="Mute",command = demo)
edit_menu.add_separator()

root.mainloop()