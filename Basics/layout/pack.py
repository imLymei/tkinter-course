import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Pack')
window.geometry('800x450')

# widgets
label1 = ttk.Label(window, text='First label', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Last of the labels', background='green')
button = ttk.Button(window, text='Button')

# layout
# label1.pack(side='top', fill='x', ipady=20)
# label2.pack(side='top', expand=True,fill='both')
# label3.pack(side='top', expand=True, fill='both', pady=20, padx=20)
# button.pack(side='top', fill='x')

label1.pack(side='top', expand=True, fill='both', padx=10, pady=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')

window.mainloop()
