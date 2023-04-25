import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Toggling Widgets')
window.geometry('200x200')


# place
# def toggle_label_place():
#     global is_label_visible
#     if (is_label_visible):
#         label.place_forget()
#         is_label_visible = False
#     else:
#         label.place(relx=0.5, rely=0.5, anchor='center')
#         is_label_visible = True


# button = ttk.Button(window, text='Toggle Label', command=toggle_label_place)
# button.place(relx=0.5, rely=0.9, anchor='center')

# is_label_visible = True
# label = ttk.Label(window, text='A Label')
# label.place(relx=0.5, rely=0.5, anchor='center')


# grid
# def toggle_label_grid():
#     global is_label_visible
#     if is_label_visible:
#         label.grid_forget()
#         is_label_visible = False
#     else:
#         label.grid(column=1, row=0)
#         is_label_visible = True


# window.columnconfigure((0, 1), weight=1, uniform='a')
# window.rowconfigure(0, weight=1, uniform='a')

# button = ttk.Button(window, text='Toggle Label', command=toggle_label_grid)
# button.grid(column=0, row=0)

# is_label_visible = True
# label = ttk.Label(window, text='A Label')
# label.grid(column=1, row=0)

# pack
def toggle_label_pack():
    global is_label_visible
    if is_label_visible:
        label.pack_forget()
        is_label_visible = False
    else:
        label.pack(pady=10)
        is_label_visible = True


button = ttk.Button(window, text='Toggle Label', command=toggle_label_pack)
button.pack(side='bottom', pady=10)

is_label_visible = True
label = ttk.Label(window, text='A Label')
label.pack(pady=10)

window.mainloop()
