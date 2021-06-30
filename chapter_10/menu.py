from tkinter import *
from tkinter import ttk


def open_file(**kwargs):
    print("Opening a file!")
    try:
        name = kwargs["file"]
    except KeyError:
        print("file picker")
    else:
        print(name)


def close_file():
    print("Closing")
    exit()


def open_file_command(file):
    def inner():
        open_file(file=file)
    return inner


root = Tk()
root.option_add("*tearOff", FALSE)

menubar = Menu(root)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label="File")
menubar.add_cascade(menu=menu_edit, label="Edit")

menu_recent = Menu(menu_file)
for f in ("file1.txt", "file2.txt"):
    menu_recent.add_command(label=f, command=open_file_command(f))

menu_file.add_command(label="Open...", command=open_file, accelerator="Ctrl + O", underline=0)
menu_file.add_cascade(menu=menu_recent, label="Recent")
menu_file.add_separator()
menu_file.add_command(label="Close", command=close_file)



root["menu"] = menubar

root.mainloop()