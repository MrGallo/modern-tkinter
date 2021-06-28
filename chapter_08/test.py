from tkinter import *
from tkinter import ttk


class MyApp:
    def __init__(self, root):
        # global name_var
        main = ttk.Frame(root)

        name_var = StringVar(value="Testing 123")
        main.grid(column=0, row=0)

        label = ttk.Label(main, textvariable=name_var)
        label.grid(column=0, row=0)


if __name__ == "__main__":
    root = Tk()
    MyApp(root)
    root.mainloop()
