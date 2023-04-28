import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ExtraWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Extra window')
        self.geometry('800x600')
        ttk.Label(self, text='Label').pack()
        ttk.Button(self, text='A button').pack()


def create_messagebox():
    answer = messagebox.askquestion('Title', 'String Body')
    print(answer)

    # messagebox.showerror('Some info', 'This is the info')


def create_window():
    global extra_window
    extra_window = ExtraWindow()


def close_window():
    extra_window.destroy()


window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

button1 = ttk.Button(window, text='Open new window', command=create_window)
button1.pack(expand=True, ipadx=20, ipady=20)

button2 = ttk.Button(window, text='Close new window', command=close_window)
button2.pack(expand=True, ipadx=20, ipady=20)

button3 = ttk.Button(
    window, text='Create [Yes/No] window', command=create_messagebox)
button3.pack(expand=True, ipadx=20, ipady=20)

window.mainloop()
