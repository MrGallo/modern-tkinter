from tkinter import *
from tkinter import ttk


def handle_listbox_select(listbox, choices, statusvar):
    i, *_ = listbox.curselection()
    statusvar.set(f"Selected: {choices[i]}.")


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root)

statusvar = StringVar(value="Select an item...")
status_bar = ttk.Label(main_frame, textvariable=statusvar, anchor=W)

choices = [f"{n} of 100" for n in range(1, 101)]
choices_var = StringVar(value=choices)
listbox = Listbox(main_frame, listvariable=choices_var)
scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=listbox.yview)
listbox.configure(yscrollcommand=scroll.set)


main_frame.grid(column=0, row=0, sticky=(N, W, S, E))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=0)

listbox.grid(column=0, row=0, sticky=(N, E, S, W))
scroll.grid(column=1, row=0, sticky=(N, E, S))

status_bar.grid(column=0, row=1, columnspan=2, sticky=(W, S, E))

listbox.bind("<<ListboxSelect>>", lambda e: handle_listbox_select(listbox, choices, statusvar))

root.mainloop()