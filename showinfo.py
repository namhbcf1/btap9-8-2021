import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror,showwarning,showinfo

root = tk.Tk()
root.title('Tkinter Messagebox')
root.resizable(0,0)
root.geometry('300x150')

options = {'fill': 'both','padx':10,'pady':10,'ipadx':5}

ttk.Button(
    root,text = 'Show an error message',
    command=lambda:showerror(
        title='error',
        message='this is an error message.')
).pack(options)
ttk.Button(
    root,text = 'Show an info message',
    command=lambda:showinfo(
        title='info',
        message='this is an showinfo message.')
).pack(options)
ttk.Button(
    root,text = 'Show an warning message',
    command=lambda:showwarning(
        title='warning',
        message='this is an warning message.')
).pack(options)

root.mainloop()