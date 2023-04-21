import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tabs')
window.geometry('400x225')

# Tab Widget
notebook = ttk.Notebook(window)

# Tab One
tab1 = ttk.Frame(notebook)
label_tab_one = ttk.Label(tab1, text='Text in Tab One')
label_tab_one.pack()
button_tab_one = ttk.Button(tab1, text='Button Tab One')
button_tab_one.pack()

tab2 = ttk.Frame(notebook)
label_tab_two = ttk.Label(tab2, text='Text in Tab Two')
label_tab_two.pack()
entry_tab_two = ttk.Entry(tab2)
entry_tab_two.pack()

notebook.add(tab1, text='Tab One')
notebook.add(tab2, text='Tab Two')
notebook.pack()


window.mainloop()
