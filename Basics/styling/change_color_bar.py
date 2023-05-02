# ONLY IN WINDOWS

import customtkinter as ctk

app = ctk.CTk(fg_color='#f0f')
app.geometry('300x200')

# DO NOT CRASH IF NOT WINDOWS
try:
    from ctypes import windll, byref, sizeof, c_int

    # change the titlebar
    HWND = windll.user32.GetParent(app.winfo_id())
    title_bar_color = 0x00E000E0  # -> FF00FF
    title_text_color = 0x000000FF  # -> FF00FF

    windll.dwmapi.DwmSetWindowAttribute(HWND, 35,
                                        byref(c_int(title_bar_color)),
                                        sizeof(c_int))
    # windll.dwmapi.DwmSetWindowAttribute(HWND, 36,
    #                                    byref(c_int(title_text_color)),
    #                                    sizeof(c_int))
except:
    pass

app.mainloop()
