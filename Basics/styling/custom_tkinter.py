import customtkinter as ctk


def handle_theme():
    global is_dark_theme
    if is_dark_theme:
        ctk.set_appearance_mode('light')
        is_dark_theme = False
    else:
        ctk.set_appearance_mode('dark')
        is_dark_theme = True


window = ctk.CTk()
window.title('Customtkinter App')
window.geometry('600x400')

string_var = ctk.StringVar(value='A String')
label = ctk.CTkLabel(window, text='A CTk Label',
                     fg_color=('blue', 'red'), corner_radius=10,
                     textvariable=string_var)
label.pack()

is_dark_theme = True

button = ctk.CTkButton(window, text='A Button',
                       fg_color='#FF0', text_color='#000',
                       hover_color='#BB0',
                       command=lambda: handle_theme())
button.pack()

frame = ctk.CTkFrame(window)
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack()

switch = ctk.CTkSwitch(frame, text='Exercise Switch',
                       fg_color='red', progress_color='pink',
                       button_color='green', button_hover_color='yellow',
                       switch_width=60, corner_radius=5)
switch.pack()

window.mainloop()
