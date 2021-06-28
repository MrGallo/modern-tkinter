from tkinter import *
from tkinter import ttk


def handle_scale_change(value):
    red.set(int(float(value)))


root = Tk()
red = IntVar(value=128)

scale = ttk.Scale(root, orient=HORIZONTAL, from_=0.0, to=255.0, command=handle_scale_change)
scale.grid(column=0, row=0, sticky=(E, W))
scale.set(128)

label = ttk.Label(root, textvariable=red)
label.grid(column=0, row=1)

root.mainloop()