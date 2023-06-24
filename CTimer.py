import threading
import time
import tkinter as tk
from tkinter import ttk

from playsound import playsound

baseWindow = tk.Tk()

ZEROS = "0"

def get_time_inputs():
    return (
        hours_input.get().strip(),
        minutes_input.get().strip(),
        secs_input.get().strip(),
    )


def reset_placeholder(event):
    hours, minutes, secs = get_time_inputs()
    if hours in [ZEROS, ""] or not hours.isnumeric():
        hours_input.delete(0, "end")
        hours_input.insert(0, ZEROS)
    if minutes in [ZEROS, ""] or not minutes.isnumeric():
        minutes_input.delete(0, "end")
        minutes_input.insert(0, ZEROS)
    if secs in [ZEROS, ""] or not secs.isnumeric():
        secs_input.delete(0, "end")
        secs_input.insert(0, ZEROS)


def start_timer():
    hours, mins, secs = [int(i) for i in get_time_inputs()]
    m, secs = divmod(secs, 60)
    mins += m

    timer_UI = tk.Toplevel(master=baseWindow)
    timer_UI.resizable(False, False)

    base_frame = tk.Frame(timer_UI)
    base_frame.pack(pady=20, padx=10)

    timeLabel = tk.Label(base_frame, text=f"{hours:02d}:{mins:02d}:{secs:02d}", font=('Arial', 24))
    timeLabel.grid(row=0, column=0)

    while (hours != 0) or (mins != 0) or (secs != 0):
        if (mins == 0) and (hours > 0):
            mins += 60
            hours -= 1

        if (secs == 0) and (mins > 0):
            mins -= 1
            secs += 60

        time.sleep(1)
        secs -= 1
        print(f"{hours:02d}:{mins:02d}:{secs:02d}")
        timeLabel.config(text=f"{hours:02d}:{mins:02d}:{secs:02d}")

    timeLabel.config(text='Time up!!!')
    playsound('./sounds/digital-alarm.mp3')
    timer_UI.destroy()


def start_timer_UI():
    t = threading.Thread(target=start_timer, daemon=True)
    t.start()


title = tk.Label(baseWindow, text="Countdown Timer", font=("Arial", 24))
title.pack(pady=10, padx=10)

time_frame = tk.Frame(baseWindow)
time_frame.pack()

hours_frame = tk.Frame(time_frame)
hours_frame.grid(row=0, column=0)
tk.Label(hours_frame, text="Hours").pack()
hours_input = tk.Entry(hours_frame, width=5, justify=tk.CENTER)
hours_input.insert(0, ZEROS)
hours_input.pack()

tk.Label(time_frame, text=":").grid(row=0, column=1, sticky=tk.N)

minutes_frame = tk.Frame(time_frame)
minutes_frame.grid(row=0, column=2)
tk.Label(minutes_frame, text="Minutes").pack()
minutes_input = tk.Entry(minutes_frame, width=5, justify=tk.CENTER)
minutes_input.insert(0, ZEROS)
minutes_input.pack()

tk.Label(time_frame, text=":").grid(row=0, column=3, sticky=tk.N)

secs_frame = tk.Frame(time_frame)
secs_frame.grid(row=0, column=4)
tk.Label(secs_frame, text="Seconds").pack()
secs_input = tk.Entry(secs_frame, width=5, justify=tk.CENTER)
secs_input.insert(0, ZEROS)
secs_input.pack()

btn_frame = tk.Frame(baseWindow)
btn_frame.pack(pady=10, padx=10, fill=tk.BOTH)

start_btn = tk.Button(btn_frame, text="Start", width=7, command=start_timer_UI)
start_btn.pack(fill=tk.X)


# input event bindings
hours_input.bind("<FocusOut>", reset_placeholder)
minutes_input.bind("<FocusOut>", reset_placeholder)
secs_input.bind("<FocusOut>", reset_placeholder)
start_btn.bind("<Enter>", reset_placeholder)

baseWindow.mainloop()
