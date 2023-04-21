import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Menus')
window.geometry('800x450')

items = ('USA', 'CAN', 'BR', 'CHN', 'MEX')

# Combobox
food_var = tk.StringVar(value='Selecione Seu Pais')
combo = ttk.Combobox(window, values=items,
                     textvariable=food_var, state='readonly')
combo.pack()

combo_label = tk.Label(window, text='a label')
combo_label.pack()

# Spinbox
int_var = tk.IntVar(value=0)
spin = ttk.Spinbox(window, from_=0, to=10, textvariable=int_var,
                   command=lambda: print('The value has changed'))
spin.pack()

# Events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(
    text=f'Voce escolheu {food_var.get()}'))
spin.bind('<<Increment>>', lambda event: print('UP'))
spin.bind('<<Decrement>>', lambda event: print('DOWN'))

window.mainloop()
