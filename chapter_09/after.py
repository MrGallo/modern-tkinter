from tkinter import *
from tkinter import ttk

def start():
    global interrupt
    button.config(text="Stop", command=stop)
    label["text"] = "Loading..."
    interrupt = False
    root.after(1, step)

def stop():
    global interrupt
    interrupt = True

def step(count=0):
    global interrupt
    if interrupt:
        answer(None)
        return

    root.after(100)
    progbar["value"] = count

    if count >= 20:
        answer(43)
        return
    
    scheduled = root.after(1, lambda: step(count + 1))
    print(scheduled)

def answer(value):
    progbar["value"] = 0
    button.config(text="Start", command=start)
    if value is None:
        label['text'] = "Interrupted."
    else:
        label['text'] = value
    


root = Tk()

frame = ttk.Frame(root, padding="5 3 5 3")
label = ttk.Label(frame, text="", anchor="center")
button = ttk.Button(frame, text="Start", command=start)
progbar = ttk.Progressbar(frame, orient=HORIZONTAL, mode="determinate", maximum=20)

frame.grid(column=0, row=0, sticky=(N, E, W, S))
label.grid(column=0, row=0, sticky=(W, E))
button.grid(column=0, row=1, sticky=(W, E))
progbar.grid(column=0, row=2, sticky=(W, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

root.mainloop()