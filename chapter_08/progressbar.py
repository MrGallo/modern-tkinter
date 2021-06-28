from tkinter import *
from tkinter import ttk
import time

def handle_button_click():
    progress.set(0)
    for _ in range(101):
        progress.set(progress.get() + 1)

root = Tk()

indeterminate = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode="indeterminate")
progress = IntVar()
determinate = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode="determinate", variable=progress)
button_go = ttk.Button(root, text="GO", command=handle_button_click)

indeterminate.grid()
determinate.grid(row=1)
button_go.grid(row=2, sticky=(W, E))

indeterminate.start()
root.mainloop()