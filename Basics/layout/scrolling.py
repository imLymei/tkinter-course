import tkinter as tk
from tkinter import ttk
from random import randint, choice

window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

# canvas
# canvas = tk.Canvas(window, bg='white', scrollregion=(0, 0, 2000, 5000))
# canvas.create_line(0, 0, 2000, 5000, fill='green', width=10)
# for i in range(100):
#     left = randint(0, 2000)
#     top = randint(0, 5000)
#     right = left + randint(10, 500)
#     bottom = top + randint(10, 500)

#     color = choice(('red', 'green', 'blue', 'orange', 'purple'))

#     canvas.create_rectangle(left, top, right, bottom, fill=color)
# canvas.pack(expand=True, fill='both')

# # mouse wheel scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(
#     int(-event.delta / 60), "units"))

# canvas.bind('<Shift-MouseWheel>', lambda event: canvas.xview_scroll(
#     int(-event.delta / 60), "units"))


# # scrollbar
# scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
# canvas.configure(yscrollcommand=scrollbar.set)
# scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

# scrollbar_horizontal = ttk.Scrollbar(
#     window, orient='horizontal', command=canvas.xview)
# canvas.configure(xscrollcommand=scrollbar_horizontal.set)
# scrollbar_horizontal.place(relx=0, rely=1, relwidth=1, anchor='sw')

# text
# text = tk.Text(window)
# for i in range(1, 200):
#     text.insert(f'{i}.0', f'Text number {i}\n')
# text.pack(expand=True, fill='both')

# scrollbar_text = ttk.Scrollbar(window, orient='vertical', command=text.yview)
# text.configure(yscrollcommand=scrollbar_text.set)
# scrollbar_text.place(relx=1, rely=0, relheight=1, anchor='ne')

# treeview
table = ttk.Treeview(window, columns=(1, 2), show='headings')
table.heading(1, text='First Name')
table.heading(2, text='Last Name')

first_names = ['Bob', 'Maria', 'Alez', 'James',
               'Martin', 'Gules', 'Anthony', 'Marcos']
last_names = ['Smith', 'Suares', 'Browson',
              'Thompshom', 'Vieira', 'Santos', 'Hunter']

for i in range(100):
    table.insert(parent='', index=tk.END, values=(
        choice(first_names), choice(last_names)))
table.pack(expand=True, fill='both')

scrollbar_table = ttk.Scrollbar(window, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor='ne')

window.mainloop()
