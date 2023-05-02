import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


# def stretch_image(event):
#     global resized_image_tk
#
#     width = event.width
#     height = event.height
#
#     resized_image = image_original.resize((width, height))
#     resized_image_tk = ImageTk.PhotoImage(resized_image)
#     canvas.create_image(0, 0, image=resized_image_tk, anchor='nw')


def fill_image(event):
    global resized_image_tk

    canvas_ratio = event.width/event.height

    if canvas_ratio > image_ratio:
        # wider
        width = int(event.width)
        height = int(width/image_ratio)
    else:
        # tiner
        height = int(event.height)
        width = int(image_ratio*height)

    resized_image = image_original.resize((width, height))
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width/2), int(event.height/2),
                        image=resized_image_tk, anchor='center')


def fit_image(event):
    global resized_image_tk

    canvas_ratio = event.width/event.height

    if canvas_ratio > image_ratio:
        height = int(event.height)
        width = int(height * image_ratio)
    else:
        width = int(event.width)
        height = int(width / image_ratio)

    resized_image = image_original.resize((width, height))
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width / 2), int(event.height / 2),
                        image=resized_image_tk, anchor='center')


window = tk.Tk()
window.geometry('600x400')
window.title('Images')

window.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')

# import a image
image_original = Image.open('../src/enxoval-para-gato-Copia.jpg')
# image_tk = ImageTk.PhotoImage(image_original)
image_ratio = image_original.size[0]/image_original.size[1]
resized_image_tk = None

python_dark = Image.open('../src/Python_icon_(black_and_white).svg.png').resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

python_icon = ctk.CTkImage(light_image=Image.open('../src/Python_icon_(black_and_white).svg.png'),
                           dark_image=Image.open('../src/Python_icon_(white).svg'))

# widgets
# label = ttk.Label(window, text='Cat', image=image_tk)
# label.pack()

button_frame = ttk.Frame(window)
button_frame.grid(column=0, row=0, sticky='nswe')

button = ttk.Button(button_frame, text='A Button', image=python_dark_tk, compound='left')
button.pack(pady=10)

button_ctk = ctk.CTkButton(button_frame, text='A Button', image=python_icon, compound='left')
button_ctk.pack(pady=10)

canvas = tk.Canvas(window, background='black', bd=0, highlightthickness=0)
canvas.grid(column=1, columnspan=3, row=0, sticky='nswe')

canvas.bind('<Configure>', fit_image)

window.mainloop()
