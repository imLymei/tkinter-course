import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Canvas')
window.geometry('800x450')

canvas = tk.Canvas(window, bg='white')
canvas.pack()

# --Canvas introduction--
# canvas.create_rectangle(
#     (50, 20, 100, 100), fill='white', width=1, dash=(1, 2), outline='blue')
# canvas.create_line(0, 0, 100, 20, fill='blue')
# canvas.create_oval((200, 0, 100, 100))
# canvas.create_arc((200, 0, 100, 100), fill='red',
#   start = 180, extent = 180, style = tk.ARC, outline = 'blue', width = 5)
# canvas.create_polygon((0, 0, 10, 200, 300, 50), fill='grey')

# canvas.create_text(
# (canvas.winfo_reqwidth()//2, canvas.winfo_reqheight()//2), text='Hello World! Iam at the middle', width=100)

# canvas.create_window((50, 100), window=ttk.Button(
# window, text='text in the canvas'))

# print(canvas.winfo_reqwidth())

# --Paint App--


def handle_mouse(event):
    size = brush_size
    if event.state == 256 or event.num == 1:
        canvas.create_oval(
            (event.x-size, event.y-size, event.x+size, event.y+size), fill='black')

    elif event.state == 1024 or event.num == 3:
        canvas.create_oval(
            (event.x-size, event.y-size, event.x+size, event.y+size), fill='white', outline='white')


def adjust_brush_size(event):
    global brush_size
    if event.delta > 0:
        brush_size += 0.5
    else:
        if brush_size > 1:
            brush_size -= 0.5


brush_size = 1

canvas.bind('<Button>', handle_mouse)
canvas.bind('<Motion>', handle_mouse)
canvas.bind('<MouseWheel>', adjust_brush_size)

window.mainloop()
