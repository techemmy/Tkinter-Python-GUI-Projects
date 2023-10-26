import customtkinter as ctk
import time
import threading
from playsound import playsound

baseWindow = ctk.CTk()
baseWindow.title("Countdown Timer")
baseWindow.resizable(False, False)

ZEROS = "00"


def get_time_inputs():
    return (
        hours_input.get().strip(),
        minutes_input.get().strip(),
        secs_input.get().strip(),
    )


def reset_entries(event):
    hours, minutes, secs = get_time_inputs()
    if hours == "" or not hours.isnumeric():
        hours_input.delete(0, "end")
        hours_input.insert(0, ZEROS)
    if minutes == "" or not minutes.isnumeric():
        minutes_input.delete(0, "end")
        minutes_input.insert(0, ZEROS)
    if secs == "" or not secs.isnumeric():
        secs_input.delete(0, "end")
        secs_input.insert(0, ZEROS)


def start_timer():
    hours, mins, secs = [int(i) for i in get_time_inputs()]
    m, secs = divmod(secs, 60)
    mins += m

    timer_UI = ctk.CTkToplevel(master=baseWindow)
    timer_UI.resizable(False, False)

    base_frame = ctk.CTkFrame(timer_UI)
    base_frame.pack(pady=20, padx=10)

    timeLabel = ctk.CTkLabel(
        base_frame, text=f"{hours:02d}:{mins:02d}:{secs:02d}", font=("Arial", 24)
    )
    timeLabel.grid(row=0, column=0)

    while (hours != 0) or (mins != 0) or (secs != 0):
        if (mins == 0) and (hours > 0):
            hours -= 1
            mins += 60

        if (secs == 0) and (mins > 0):
            mins -= 1
            secs += 60

        time.sleep(1)
        secs -= 1
        timeLabel.configure(text=f"{hours:02d}:{mins:02d}:{secs:02d}")

    timeLabel.configure(text="Time up!!!")
    playsound("./sounds/digital-alarm.mp3")
    timer_UI.destroy()


def start_timer_UI():
    t = threading.Thread(target=start_timer, daemon=True)
    t.start()


title = ctk.CTkLabel(baseWindow, text="Countdown Timer", font=("Arial", 24))
title.pack(pady=10, padx=10)

time_frame = ctk.CTkFrame(baseWindow)
time_frame.pack(padx=20)

hours_frame = ctk.CTkFrame(time_frame)
hours_frame.grid(row=0, column=0, padx=5, pady=5, ipady=5)
ctk.CTkLabel(hours_frame, text="Hours").pack(padx=20)
hours_input = ctk.CTkEntry(hours_frame, width=5, justify=ctk.CENTER)
hours_input.insert(0, ZEROS)
hours_input.pack(ipadx=10)

ctk.CTkLabel(time_frame, text=":").grid(row=0, column=1)

minutes_frame = ctk.CTkFrame(time_frame)
minutes_frame.grid(row=0, column=2, padx=5, pady=5, ipady=5)
ctk.CTkLabel(minutes_frame, text="Minutes").pack(padx=20)
minutes_input = ctk.CTkEntry(minutes_frame, width=5, justify=ctk.CENTER)
minutes_input.insert(0, ZEROS)
minutes_input.pack(ipadx=10)

ctk.CTkLabel(time_frame, text=":").grid(row=0, column=3)

secs_frame = ctk.CTkFrame(time_frame)
secs_frame.grid(row=0, column=4, padx=5, pady=5, ipady=5)
ctk.CTkLabel(secs_frame, text="Seconds").pack(padx=20)
secs_input = ctk.CTkEntry(secs_frame, width=5, justify=ctk.CENTER)
secs_input.insert(0, ZEROS)
secs_input.pack(ipadx=10)

btn_frame = ctk.CTkFrame(baseWindow)
btn_frame.pack(pady=10, padx=20, fill=ctk.BOTH)

start_btn = ctk.CTkButton(btn_frame, text="Start", width=7, command=start_timer_UI)
start_btn.pack(fill=ctk.X)

hours_input.bind("<FocusOut>", reset_entries)
minutes_input.bind("<FocusOut>", reset_entries)
secs_input.bind("<FocusOut>", reset_entries)
start_btn.bind("<Enter>", reset_entries)


baseWindow.mainloop()
