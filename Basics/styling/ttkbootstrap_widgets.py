import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

window = ttk.Window(themename='darkly')
window.title('Extra Widgets')

# scroll frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill='both')

for i in range(100):
    ttk.Label(scroll_frame, text=f'The {i}th Label').pack()
    ttk.Button(scroll_frame, text=f'The {i}th Checkbutton').pack()

# toast
toast = ToastNotification(title='This is a message', message='Thi is the actual message', duration=5000,
                          bootstyle='dark', position=(10, 10, 'ne'))
ttk.Button(window, text='Show Toast', command=toast.show_toast).pack(pady=10)

# tooltip
checkbutton = ttk.Checkbutton(window, text='Do something?', bootstyle='warning')
checkbutton.pack()
ToolTip(checkbutton, text='This do nothing', bootstyle='danger')

# calendar
calendar = DateEntry(window)
calendar.pack()
ttk.Button(window, text='Get Date', command=lambda:print(calendar.entry.get())).pack()

# progressbar -> floodgauge
progress_int = tk.IntVar(value=50)
floodgauge = Floodgauge(window, text='Progress', variable=progress_int, mask='Downloading... {}%')
floodgauge.pack(pady=10, fill='x')
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack(fill='x')

# meter
meter = ttk.Meter(window, amounttotal=100, amountused=10, interactive=True, metertype='semi', subtext='km/h')
meter.pack()

window.mainloop()
