"""import tkinter as tk

from tkinter import PhotoImage

root=tk.Tk()
image=PhotoImage(file="image.png")
label=tk.Label(root,image=image)
label.pack()
root.mainloop()"""
import tkinter as tk


root=tk.Tk()
root.title("Greeting Program")

label=tk.Label(root,text="Enter your name:")
label.pack()

entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text="Greet command=greet")
entry.pack()

def greet():
    name=entry.get()
    if name:
        greeting=f"Hello,{name}!"
    else:
        Greeting="Please enetr your name!"
        label=config(text=greeting)

root.mainloop()