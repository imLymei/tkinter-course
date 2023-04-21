import tkinter as tk
from tkinter import ttk


#* experimenting with some types of buttons


#! Window
window = tk.Tk()
window.title('Buttons')
window.geometry('150x100')


#? Widgets
#?  Button
button = ttk.Button(
    window,
    text = 'A simple button',
    command = lambda:print('A simple button was pressed')
    )
button.pack()

#?  Checkbutton
check_variable = tk.BooleanVar()
check = ttk.Checkbutton(
    window,
    text = 'Checkbox 1',
    command = lambda:print(f'Checkbutton 1 was pressed and its {check_variable.get()}'),
    variable = check_variable
    )
check.pack()

#?  Radiobuttons
radio_variable = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'Radiobutton 1',
    value = 'radio 1',
    variable = radio_variable,
    command = lambda:print(radio_variable.get())
    )
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text = 'Radiobutton 2',
    value = 2,
    variable = radio_variable,
    command = lambda:print(radio_variable.get())
    )
radio2.pack()


#! Main loop
window.mainloop()
