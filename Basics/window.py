import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window_width = 400
window_width_offset = (window.winfo_screenwidth()//2) - (window_width//2)
window_height = 225
window_height_offset = (window.winfo_screenheight()//2) - (window_height//2)
window_geometry_data = f'{window_width}x{window_height}+{window_width_offset}+{window_height_offset}'

window.title('More Window Changes')
window.geometry(window_geometry_data)
window.iconbitmap('src/console.ico')

# Window size config
window.minsize(160, 90)
# window.maxsize(1600, 900)
# window.resizable(False, False)

# Screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Window attributes
window.attributes('-alpha', 1)
# window.attributes('-topmost', True)  # Window always on top

# Security event
window.bind('<Escape>', lambda envet: window.quit())

# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)

# Title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se')

window.mainloop()
