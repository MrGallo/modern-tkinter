from tkinter import *
from tkinter import ttk


def handle_spin_change(choice, label):
    label.config(text=f"Choice: {choice.get()}.")
    


root = Tk()
choices = "One Two Three".split(" ")
choice = StringVar()

spin = ttk.Spinbox(root, textvariable=choice, values=choices, wrap=True, command=lambda: handle_spin_change(choice, label))
spin.state(["readonly"]) # use can't enter their own value.

label = ttk.Label(root, text="Make a choice", anchor=W)

spin.grid()
label.grid(row=1, sticky=(W, E))

root.mainloop()