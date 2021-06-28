from tkinter import *
from tkinter import ttk


class BindingEvents:
    def __init__(self, root):
        self.root = root
        self.label = ttk.Label(root, text="Starting...")
        self.label.grid()

        self.label.bind('<Enter>', lambda e: self.label.configure(text='Moved mouse inside'))
        self.label.bind('<Leave>', lambda e: self.label.configure(text='Moved mouse outside'))
        self.label.bind('<ButtonPress-1>', lambda e: self.label.configure(text='Clicked left mouse button'))
        self.label.bind('<3>', lambda e: self.label.configure(text='Clicked right mouse button'))
        self.label.bind('<Double-1>', lambda e: self.label.configure(text='Double clicked'))
        self.label.bind('<B3-Motion>', lambda e: self.label.configure(text=f"right button drag to {e.x},{e.y}"))
        self.label.bind('<Key-A>', lambda e: self.label.configure(text="Pressed A"))


if __name__ == "__main__":
    root = Tk()
    BindingEvents(root)
    root.mainloop()