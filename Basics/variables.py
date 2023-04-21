import tkinter as tk
from tkinter import ttk


#* experimenting with tk variables


def button_func():
    print(string_var.get())
    string_var.set('Button pressed')


#! Window
window = tk.Tk()
window.title('Tkinter variable')


#? Widgets
#?  tkinter variable
string_var = tk.StringVar(value = 'Change me')

#?  Label
label = ttk.Label(master = window, textvariable = string_var)
label.pack()

#?  Text input
entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

#? Button
button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()


#! Main loop
window.mainloop()
