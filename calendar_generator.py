import customtkinter as ctk
import calendar

def generate_calendar():
	new_cal.configure(text=calendar.month(int(year.get()), int(month.get())))

root = ctk.CTk()
root.resizable(False, False)

ctk.CTkLabel(root, text="Generate calendar").grid(row=0, columnspan=2)

ctk.CTkLabel(root, text="Choose Month").grid(row=1, column=0)
ctk.CTkLabel(root, text="Enter Year").grid(row=1, column=1)

month = ctk.CTkOptionMenu(root, values=[str(i) for i in range(1, 13)])
month.grid(row=2, column=0, padx=10)

year = ctk.CTkEntry(root)
year.grid(row=2, column=1, padx=10)

ctk.CTkButton(root, text="Generate", command=generate_calendar).grid(
    row=3, columnspan=2, padx=10, pady=20, sticky=ctk.NSEW
)

new_cal = ctk.CTkLabel(root, 
	text=calendar.month(
		calendar.datetime.date.today().year,
		calendar.datetime.date.today().month
		)
	)
new_cal.grid(row=4, columnspan=2, sticky=ctk.NSEW)

root.mainloop()