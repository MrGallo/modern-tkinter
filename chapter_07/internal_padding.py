from tkinter import *
from tkinter import ttk


root = Tk()
root.minsize(640, 480)
frame_main = ttk.Frame(root, width=640, height=480)
frame_main.grid(row=0, column=0, sticky="nwes")

s = ttk.Style()
s.configure('FrameLeft.TFrame', background="red")
s.configure('FrameRight.TFrame', background="blue")

ttk.Frame(frame_main, width=100, height=100, style="FrameLeft.TFrame").grid(row=0, column=0, padx=20, pady=20, sticky="")
ttk.Frame(frame_main, width=100, height=100, style="FrameRight.TFrame").grid(row=0, column=1, ipadx=20, ipady=20, sticky="")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame_main.columnconfigure(0, weight=1)
frame_main.columnconfigure(1, weight=1)
frame_main.rowconfigure(0, weight=1)

root.mainloop()