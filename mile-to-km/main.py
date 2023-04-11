import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def decimal_set(number,decimal_get):
    decimal = 10**decimal_get
    return (round(number*decimal)/decimal)

def convert():
    mile = input_int.get()
    km = mile*1.61
    output_string.set(f'{decimal_set(km, 2)} Km')

# Window
window = ttk.Window(themename = 'darkly')
window.title('Mile to Km converter')
window.geometry('300x150')

# Widgets
#   Title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Arial 24')
title_label.pack()

#   Text input
input_frame = ttk.Frame(master = window)
input_frame.pack()
input_int = tk.IntVar()
input_text = ttk.Entry(master = input_frame, textvariable = input_int)
input_text.pack(side = 'left', padx = 10)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
button.pack(side = 'left', pady = 10)

#   Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'output', font = 'Arial 16', textvariable = output_string)
output_label.pack(pady = 5)

# Main loop
window.mainloop()
