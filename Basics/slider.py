import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Sliders')
window.geometry('400x225')

scale_double = tk.DoubleVar(value=0)

# Slider
slider = ttk.Scale(
    window,
    command=lambda value: label.configure(
        text=f'{round(scale_double.get())}%' if scale_double.get() < 100 else 'Completed!'),
    from_=0,
    to=100,
    length=300,
    variable=scale_double
)
slider.pack()

# Progress bar
progress = ttk.Progressbar(
    window, variable=scale_double, maximum=100)
progress.pack()

label = ttk.Label(window, text=0)
label.pack()

# Scrolled text
# scrolled_text = scrolledtext.ScrolledText(window)
# scrolled_text.pack()

# Exercise
double_var = tk.DoubleVar()

progress_bar = ttk.Progressbar(
    window, maximum=100, variable=double_var, orient='vertical')
progress_bar.pack()
progress_bar.start()

percentage_label = ttk.Label(window, textvariable=double_var)
percentage_label.pack()

affected_slider = ttk.Scale(window, from_=0, to=100, variable=double_var)
affected_slider.pack()

window.mainloop()
