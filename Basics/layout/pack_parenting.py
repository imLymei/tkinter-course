import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Pack parenting')
window.geometry('450x800')

# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='First Label', background='red')
label2 = ttk.Label(top_frame, text='Label 2', background='blue')

# middle widget
label3 = ttk.Label(window, text='Another Label', background='green')

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text='Last of the Labels',
                   background='orange')
button1 = ttk.Button(bottom_frame, text='A Button')
button2 = ttk.Button(bottom_frame, text='Another Button')

# top layout
label1.pack(side='left', expand=True, fill='both')
label2.pack(side='left', expand=True, fill='both')
top_frame.pack(expand=True, fill='both')

# middle layout
label3.pack(expand=True)

# bottom layout
button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)

# exercise frame
bottom_right_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(bottom_right_frame, text='Button One')
button4 = ttk.Button(bottom_right_frame, text='Button Two')
button5 = ttk.Button(bottom_right_frame, text='Button Three')

button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
bottom_right_frame.pack(side='left', expand=True, fill='both')

window.mainloop()
