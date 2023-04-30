import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

# print(font.families())

style = ttk.Style()
# print(style.theme_names())
# style.theme_use('alt')

style.configure(
    'new.TButton',
    foreground='green',
    font=('Font Awesome 5 Brands Regular', 24)
)
style.configure(
    'TFrame',
    background='pink',
)
style.map(
    'new.TButton',
    foreground=[('pressed', 'red'), ('disabled', 'yellow')],
    background=[('pressed', 'red'), ('disabled', 'yellow')],
)

label = ttk.Label(
    window,
    text='A label',
    background='blue',
    foreground='red',
    font=('Font Awesome 5 Brands Regular', 24),
    justify='right',
)
button = ttk.Button(
    window,
    text='A button',
    style='new.TButton',
)
frame = ttk.Frame(
    window,
    height=200,
    width=200,
)

label.pack(fill='both')
button.pack()
frame.pack()

window.mainloop()
