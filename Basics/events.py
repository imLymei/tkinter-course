import tkinter as tk
from tkinter import ttk

# Events tests

window = tk.Tk()
window.title('events')
window.geometry('800x450')

text_box = tk.Text(window)
text_box.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='a button')
button.pack()

# Events
window.bind('<Shift-Control-KeyPress-S>', lambda event: print('EVENT FOUND!'))
#            <Modifiers-Type-Detail> , Function ^always receive a event parameter

# window.bind('<KeyPress>', lambda event: print(
#     f'The key {event.keysym} was pressed'))

window.mainloop()
