from tkinter import *
from tkinter import ttk


class FeetToMeters(Tk):
    def __init__(self):
        super().__init__()
        self.title("Feet to Meters")
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.feet = StringVar()
        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        ttk.Label(self.mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(self.mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(self.mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(self.mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.feet_entry.focus()
        self.bind("<Return>", self.calculate)
    
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass


if __name__ == "__main__":
    app = FeetToMeters()
    app.mainloop()