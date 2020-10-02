import shutil
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

root = tk.Tk()

sourcePath = filedialog.askdirectory()
receivePath = filedialog.askdirectory()

file_names = os.listdir(sourcePath)

root.title("Michaels File Organizer!")

#VVV This class is the window VVV
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.testhi = tk.Button(self)
        self.testhi["text"] = "Move!" #button that calles the .movefiles command that is connected to the code that moves the files to the destination folder
        self.testhi["command"] = self.movefiles
        self.testhi.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def movefiles(self):
        for file_name in file_names:
            shutil.move(os.path.join(sourcePath, file_name), receivePath) #moves files from specifid source folder to specified destination folder

root = tk.Tk()
app = Application(master=root)
app.mainloop()
