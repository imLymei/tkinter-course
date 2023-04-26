import tkinter as tk
from tkinter import ttk


# def create_segment(parent, button_text):
#     frame = ttk.Frame(parent)

#     ttk.Entry(frame).pack(expand=True, fill='both')
#     ttk.Button(frame, text=button_text).pack(expand=True, fill='both')

#     return frame


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, entry_button_text):
        super().__init__(parent)

        # grid layout
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')

        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
        self.create_segment(self, entry_button_text).grid(
            row=0, column=2, sticky='nswe')

        self.pack(expand=True, fill='both', padx=10, pady=10)

    def create_segment(self, parent, button_text):
        frame = ttk.Frame(parent)

        ttk.Entry(frame).pack(expand=True, fill='both')
        ttk.Button(frame, text=button_text).pack(expand=True, fill='both')

        return frame


window = tk.Tk()
window.title('Widgets and return')
window.geometry('400x600')

# widgets
Segment(window, 'Label', 'Button', 'Entry Button 1')
Segment(window, 'Test', 'Click', 'Entry Button 2')
Segment(window, 'Hello', 'Test', 'Entry Button 3')
Segment(window, 'Bye', 'Launch', 'Entry Button 4')
Segment(window, 'Last One', 'Exit', 'Entry Button 5')

window.mainloop()
