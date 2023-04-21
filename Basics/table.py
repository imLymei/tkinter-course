import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.title('Table')
window.geometry('600x400')

# data
first_name = ['Bob', 'Maria', 'Alex', 'James', 'Susan',
              'Henry', 'Carlos', 'Luca', 'August', 'Nila', 'Hunter']
last_name = ['Smith', 'Tsumibito', 'Macro', 'Taylor', 'Alves', 'Cardoso',
             'Silva', 'James', 'Akira', 'Takashi', 'Silveira', 'Santos', 'Mikel']
number_sequence = ['123', '321', '777', '666', '101', '010',
                   '111', '01', '001', '000', '412', '420', '498', '972']

# Treeview
table = ttk.Treeview(window, columns=(
    'first', 'last', 'email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Last Name')
table.heading('email', text='E-mail')
table.pack(fill='both', expand=True)

# Insert values into the table
# table.insert(parent='', index=0, value=('Jhon', 'Doe', 'jhondoe777@email.com'))
for i in range(100):
    temp_first_name = choice(first_name)
    temp_last_name = choice(last_name)
    email = f'{temp_first_name}{temp_last_name}{choice(number_sequence)}@email.com'
    data = (temp_first_name, temp_last_name, email)
    table.insert(parent='', index=i, value=data)

# Events


def handle_item_selection(_):
    print('---')
    for item in table.selection():
        temp_first_name = table.item(item)["values"][0]
        temp_last_name = table.item(item)["values"][1]
        email = table.item(item)["values"][2]

        print(
            f'First Name: {temp_first_name} {temp_last_name} | E-mail: {email}')


def delete_item(_):
    selected_items = table.selection()
    print(f'{len(selected_items)} item(s) deletados')
    for item in selected_items:
        table.delete(item)


# table.selection() return hexadecimal ID
table.bind('<<TreeviewSelect>>', handle_item_selection)
table.bind('<Delete>', delete_item)

# Items

window.mainloop()
