import tkinter as tk
import customtkinter

app = customtkinter.CTk()
app.title('Simple Interest Calculator')
app.resizable(False, False)

def reset():
	princpal_input.delete(0, len(princpal_input.get()))
	interest_rate_input.delete(0, len(interest_rate_input.get()))
	years_input.delete(0, len(years_input.get()))

def calculate_amount(principal, interest_rate, years):
	try:
		if (not principal or not interest_rate or not years):
			print("yes", principal, interest_rate, years)
			raise TypeError

		principal, interest_rate, years = float(principal), float(interest_rate), float(years)
		interest = (principal * interest_rate * years) / 100
		amount = principal + interest

		tk.messagebox.showinfo("Calculated Values", 
			"The interst to pay is {0:.2f}\
			    The total amount is {1:.2f}".format(
			 	interest, amount
			 	)
			)

	except TypeError:
		tk.messagebox.showwarning("Incomplete info",
			"Make sure you type values for all fields"
			)
	except ValueError:
		tk.messagebox.showerror("Invalid input",
			"Make sure you type in numbers only"
			)


title = tk.Label(
	app, text='Calculate interest rate',
	font=('Helvetica', 20))
title.pack(pady=5)

payment_info_frame = customtkinter.CTkFrame(app)
payment_info_frame.pack(pady=10)


principal = customtkinter.CTkLabel(payment_info_frame, text='Principal:')
principal.grid(row=0, column=0, sticky=customtkinter.W, padx=5)

princpal_input = customtkinter.CTkEntry(
	payment_info_frame, placeholder_text='Enter the principal'
	)
princpal_input.grid(row=0, column=1)

interest_rate = customtkinter.CTkLabel(payment_info_frame, text='Annual Interest Rate:')
interest_rate.grid(row=1, column=0, sticky=customtkinter.W, padx=5)

interest_rate_input = customtkinter.CTkEntry(
	payment_info_frame, placeholder_text='Type interest rate...'
	)
interest_rate_input.grid(row=1, column=1, pady=10)

years = customtkinter.CTkLabel(payment_info_frame, text='Enter the years:')
years.grid(row=2, column=0, sticky=customtkinter.W, padx=5)

years_input = customtkinter.CTkEntry(
	payment_info_frame, placeholder_text='Type the year(s)...'
	)
years_input.grid(row=2, column=1)


action_btns_frame = customtkinter.CTkFrame(app)
action_btns_frame.pack(pady=10, fill="both", padx=25)

calculate_amount_btn = customtkinter.CTkButton(
	action_btns_frame,
	text='Calculate amount',
	hover_color='green',
	fg_color='#01701f',
	command=lambda: calculate_amount(
		princpal_input.get().strip(" "),
		interest_rate_input.get().strip(" "),
		years_input.get().strip(" ")
		)
	)
calculate_amount_btn.pack(fill="both")

reset_btn = customtkinter.CTkButton(
	action_btns_frame,
	text='Reset values',
	hover_color='grey',
	fg_color='white',
	text_color='black',
	command=reset
	)
reset_btn.pack(fill="both", pady=5)

app.mainloop()