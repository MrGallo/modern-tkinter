from tkinter import *
from tkinter import ttk


class MyApp:
    def __init__(self, root):
        string_var = "Hello, World!"
        label = ttk.Label(root, text=string_var)
        label.grid()


if __name__ == "__main__":
    root = Tk()
    MyApp(root)
    root.mainloop()
