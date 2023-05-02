import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, width, orient=-1):
        super().__init__(parent)

        # general attributes
        self.orient = abs(orient)/orient
        self.start_pos = start_pos
        self.end_pos = start_pos+width*self.orient
        self.width = width

        self.step = 0.01

        self.pos = start_pos
        self.in_start_pos = True

        self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=1)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()

    def animate_forward(self):
        if ((self.pos - self.end_pos) - self.step > 0 > self.orient) or ((self.end_pos - self.pos) - self.step > 0 and self.orient > 0):
            self.pos += self.step * self.orient
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_forward)
        else:
            self.place(relx=self.end_pos, rely=0, relwidth=self.width, relheight=1)
        self.in_start_pos = False

    def animate_backward(self):
        if ((self.pos - self.start_pos) + self.step < 0 and self.orient < 0) or ((self.start_pos - self.pos) +
                                                                                 self.step < 0 < self.orient):
            self.pos -= self.step * self.orient
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_backward)
        else:
            self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=1)
        self.in_start_pos = True


# def animate_x(distance, speed, x=0):
#     half_width = button.winfo_width()/2
#     relative_x = (button.winfo_x()+half_width)/window.winfo_width()
#     final_distance = distance-speed
#
#     if x <= final_distance:
#         button.place(relx=relative_x+speed, rely=0.5, anchor='center')
#         print(f'RELX: {x+speed}')
#         window.after(10, lambda: animate_x(distance, speed, x+speed))
#     else:
#         button.place(relx=relative_x + distance-x, rely=0.5, anchor='center')
#
#
# def move_btn():
#     # layout
#     global button_x
#     button_x += 0.05
#     button.place(relx=button_x, rely=0.5, anchor='center')
#
#     # configure
#     colors = ['red', 'yellow', 'green', 'pink']
#     random_color = choice(colors)
#     button.configure(fg_color=random_color, hover_color=random_color)
#
#
# def infinite_print():
#     print('infinite')
#     window.after(1000, infinite_print)


window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

# animated widget
animate_panel = SlidePanel(window, -0.3, 0.3, 1)
ctk.CTkLabel(animate_panel, text='A label').pack(expand=True, fill='both', pady=10)
ctk.CTkLabel(animate_panel, text='A second label').pack(expand=True, fill='both', pady=10)
ctk.CTkButton(animate_panel, text='A Button').pack(expand=True, fill='both', pady=10)
ctk.CTkTextbox(animate_panel).pack(expand=True, fill='both')

# button
button_x = 0.5
button = ctk.CTkButton(window, text='Toggle Sidebar', command=animate_panel.animate, anchor='center')
button.place(relx=button_x, rely=0.5, anchor='center')

window.mainloop()
