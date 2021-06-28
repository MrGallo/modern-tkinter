from tkinter import *
from tkinter import ttk


root = Tk()
root.title = "Grid Example Complete"
frame_main = ttk.Frame(root, padding=(3, 3, 12, 12))

frame_left = ttk.Frame(frame_main, borderwidth=5, relief="ridge", width=200, height=100)
label_name = ttk.Label(frame_main, text="Name")
name = StringVar()
entry_name = ttk.Entry(frame_main, textvariable=name)

one = BooleanVar(value=True)
two = BooleanVar()
three = BooleanVar(value=True)

check_one = ttk.Checkbutton(frame_main, text="One", variable=one, onvalue=True)
check_two = ttk.Checkbutton(frame_main, text="Two", variable=two, onvalue=True)
check_three = ttk.Checkbutton(frame_main, text="Three", variable=three, onvalue=True)

button_ok = ttk.Button(frame_main, text="Okay")
button_cancel = ttk.Button(frame_main, text="Cancel")

frame_main.grid(column=0, row=0, sticky="nsew")
frame_left.grid(row=0, column=0, sticky="nsew", columnspan=3, rowspan=2)

label_name.grid(column=3, row=0, columnspan=2, sticky="nw", padx=5)
entry_name.grid(row=1, column=3, columnspan=2, sticky="new", pady=5, padx=5)

check_one.grid(column=0, row=3)
check_two.grid(column=1, row=3)
check_three.grid(column=2, row=3)

button_ok.grid(row=3, column=3)
button_cancel.grid(row=3, column=4)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame_main.columnconfigure(0, weight=3)
frame_main.columnconfigure(1, weight=3)
frame_main.columnconfigure(2, weight=3)
frame_main.columnconfigure(3, weight=1)
frame_main.columnconfigure(4, weight=1)
frame_main.rowconfigure(1, weight=1)  # expands row to fullest extent

# root.mainloop()