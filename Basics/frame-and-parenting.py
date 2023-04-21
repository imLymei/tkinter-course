import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Frame and Parenting')
window.geometry('400x225')

# Frame
frame = ttk.Frame(window, width=200, height=150,
                  borderwidth=10, relief=tk.RIDGE)
frame.pack_propagate(False)
frame.pack(side='left')

label = ttk.Label(frame, text='My text inside a frame')
label.pack()

button = ttk.Button(frame, text='Button in a frame')
button.pack()

label2 = ttk.Label(window, text='Text outside the frame')
label2.pack()

window.mainloop()
