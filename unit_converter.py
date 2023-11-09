import customtkinter as ctk
from temp_converters import *

def set_dropdown_values():
    unit = units_converter[units_menu.get()][0]
    units = tuple(unit.keys())

    from_rate.configure(values=units)
    from_rate.set(units[0])
    to_rate.configure(values=units)
    to_rate.set(units[0])

def length_converter(value, initial, final):
    return value * length[initial][final]

def temperature_converter(value, initial, final):
    return temperature[initial][final](value)

def units_menu_callback(choice):
    set_dropdown_values()
    clear_entry_text(None)

def clear_entry_text(choice):
    user_input.delete(0, ctk.END)
    conversion_output.delete(0, ctk.END)

def convert(event):
    try:
        cleaned_input = user_input.get().strip()

        if cleaned_input == "":
            clear_entry_text(None)
            return

        error_label.configure(text='')
        value = float(cleaned_input)
        initial = from_rate.get()
        final = to_rate.get()

        if initial == final:
            result = value
        else:
            converter = units_converter[units_menu.get()][1]
            result = converter(value, initial, final)

        conversion_output.delete(0, ctk.END)
        conversion_output.insert(0, result)
    except ValueError:
        error_label.configure(text='Please enter a number')

length = {
    "metre": {"kilometer": 0.001, "centimeter": 100, "millimeter": 1000},
    "kilometer": {"metre": 1000, "centimeter": 100000, "millimeter": 1000000},
    "centimeter": {"metre": 0.01, "kilometer": 0.00001, "millimeter": 10}
}

temperature = {
    "celsius" : {"fahrenheit": celsius_to_fahrenheit, "kelvin": celsius_to_kelvin},
    "fahrenheit": {"celsius": fahrenheit_to_celsius, "kelvin": fahrenheit_to_kelvin},
    "kelvin": {"celsius": kelvin_to_celsius, "fahrenheit": kelvin_to_fahrenheit}
}

units_converter = {
    "length": (length, length_converter),
    "temperature": (temperature, temperature_converter)
}

baseWindow = ctk.CTk()
baseWindow.resizable(True, False)
baseWindow.title("Convert between units")

ctk.CTkLabel(baseWindow, text='Units Converter', font=("Helvetica", 24)).pack(pady=10, padx=10)

units_menu = ctk.CTkOptionMenu(baseWindow, values=["length", "temperature"], command=units_menu_callback)
units_menu.set("length")
units_menu.pack(fill=ctk.X, pady=20, padx=10)

rates_frame = ctk.CTkFrame(baseWindow)
rates_frame.pack(fill=ctk.X)

from_rate = ctk.CTkOptionMenu(rates_frame, command=clear_entry_text)
from_rate.pack(side="left",fill=ctk.X, expand=True, pady=20, padx=10)

to_rate = ctk.CTkOptionMenu(rates_frame, command=clear_entry_text)
to_rate.pack(side="left", fill=ctk.X, expand=True, pady=20, padx=10)

input_and_output_frame = ctk.CTkFrame(baseWindow)
input_and_output_frame.pack(fill=ctk.X, pady=10)

user_input = ctk.CTkEntry(input_and_output_frame)
user_input.pack(side='left', fill=ctk.X, expand=True, padx=10)
user_input.bind('<KeyRelease>', convert)

conversion_output = ctk.CTkEntry(input_and_output_frame)
conversion_output.pack(side='right', fill=ctk.X, expand=True, padx=10)

error_label = ctk.CTkLabel(baseWindow, text='', text_color='red')
error_label.pack()

set_dropdown_values()

baseWindow.mainloop()
