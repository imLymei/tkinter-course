import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Stacking Widgets')
window.geometry('800x450')

label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='green')
label3 = ttk.Label(window, text='Label 3', background='blue')

# label1.lift()

frame = ttk.Frame(window)
button1 = ttk.Button(frame, text='Raise Label 1',
                     command=lambda: label1.lift())
button2 = ttk.Button(frame, text='Raise Label 2',
                     command=lambda: label2.lift())
button3 = ttk.Button(frame, text='Raise Label 3',
                     command=lambda: label3.lift())

label1.place(relx=0.15, rely=0.15, width=200, height=200)
label2.place(relx=0.25, rely=0.25, width=200, height=200)
label3.place(relx=0.35, rely=0.35, width=200, height=200)

frame.pack(side='right', padx=20)
button1.pack(ipadx=50, ipady=50)
button2.pack(ipadx=50, ipady=50)
button3.pack(ipadx=50, ipady=50)

window.mainloop()
