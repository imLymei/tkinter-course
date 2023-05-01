import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Colors')
window.geometry('400x300')

ttk.Label(window, background='#40A').pack(expand=True, fill='both')
ttk.Label(window, background='#4fc256').pack(expand=True, fill='both')
ttk.Label(window, background='#E8095D').pack(expand=True, fill='both')

window.mainloop()
