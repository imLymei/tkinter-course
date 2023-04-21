import tkinter as tk
from tkinter import ttk


#* creating a window and widgets, while changing its configurations


def button_func():
    # print(f'Button pressed with the value "{entry.get()}"')
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disabled'
    button['state'] = 'disabled'


#! Window creation
window = tk.Tk()
window.title('Window and Widgets')
# window.geometry('800x450')


#? Create widgets
# text_input = tk.Text(master = window)
# text_input.pack() #? Adds the widget in the actual top of the screen


#? ttk widgets
#?  ttk text
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

#?  ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#?  ttk button
button = ttk.Button(master = window, text = 'Save', command = button_func)
button.pack()


#! Main loop
window.mainloop()
