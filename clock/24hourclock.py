from tkinter import *
from tkinter import ttk

from time import strftime

root = Tk()
root.title("Michael's Clock")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 40, 'bold'),
                          background = 'blue',
                          foreground = 'black')

lbl.pack(anchor = 'center')
time()

mainloop()
