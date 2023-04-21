import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Window Menus')
window.geometry('400x225')

# Menu
menu = tk.Menu(window)

# Sub Menu
# Tearoff: Set if menu can get out of the window
file_menu = tk.Menu(menu, tearoff=False)

file_menu.add_command(label='New', command=lambda: print('New File'))
file_menu.add_command(label='Open', command=lambda: print('Open File'))
file_menu.add_separator()

menu.add_cascade(label='File', menu=file_menu)


# Another menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(
    label='Help', command=lambda: print(help_check_string.get()))

help_check_string = tk.StringVar(value='off')
help_menu.add_checkbutton(
    label='Check',
    onvalue='on',
    offvalue='off',
    variable=help_check_string
)

menu.add_cascade(label='Help', menu=help_menu)

window.configure(menu=menu)

# Menu button
menu_button = ttk.Menubutton(window, text='Menu button')
menu_button.pack()

button_menu = tk.Menu(menu_button, tearoff=False)
button_menu.add_command(label='Button Menu', command=lambda: print('buttond'))
button_menu.add_checkbutton(label='Check')

menu_submenu = tk.Menu(button_menu, tearoff=False)
menu_submenu.add_command(label='Print Hello', command=lambda: print('Hello'))
button_menu.add_cascade(label='Sub Menu', menu=menu_submenu)

menu_button['menu'] = button_menu

window.mainloop()
