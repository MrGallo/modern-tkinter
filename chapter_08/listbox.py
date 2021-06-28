from tkinter import *
from tkinter import ttk
from typing import List


def onSelectionChange(selections):
    selected_choices = []
    for i in selections:
        selected_choices.append(choices[i])

    selected.set(", ".join(selected_choices))


root = Tk()
root.minsize(400, 300)
frame_main = ttk.Frame(root)

choices = "one two three four".split()
choicesvar = StringVar(value=choices)
selected = StringVar()

lbox = Listbox(frame_main, listvariable=choicesvar, height=5, selectmode="multiple")
label = ttk.Label(frame_main, textvariable=selected)

frame_main.grid(row=0, column=0, sticky="news")
lbox.grid(row=0, column=0)
label.grid(row=0, column=1)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main.rowconfigure(0, weight=1)
frame_main.columnconfigure(0, weight=1)
frame_main.columnconfigure(1, weight=1)

lbox.bind("<<ListboxSelect>>", lambda e: onSelectionChange(lbox.curselection()))

root.mainloop()
