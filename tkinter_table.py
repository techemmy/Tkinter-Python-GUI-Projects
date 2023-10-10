import tkinter as tk
from tkinter import ttk

class TableWidget(ttk.Frame):
	def __init__(self, parent, table_data):
		super().__init__(master=parent)

		table_columns = tuple((i.lower() for i in table_data[0]))
		self.table = ttk.Treeview(self, columns=table_columns, show='headings', padding=20)

		for i in table_columns:
			self.table.heading(i, text=i.capitalize())
			self.table.column(i, anchor='center')

		self.table.tag_configure('red', background='red', foreground='white')
		self.table.tag_configure('lightblue', background='lightblue')
		self.table.tag_configure('grey', background='grey')
		self.table.tag_configure('blue', background='blue', foreground='white')

		for i in range(1, len(table_data)):
			self.table.insert('', tk.END, values=table_data[i], tag=table_data[i][-1])

		self.table.grid(row=0, column=0, sticky=tk.NSEW)
		self.pack()

	def activate_scrollbar(self):
		scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.table.yview)
		self.table.configure(yscroll=scrollbar.set)
		scrollbar.grid(row=0, column=1, sticky='ns')



baseWindow = tk.Tk()
baseWindow.title("Your first tkinter Table")

tk.Label(baseWindow, text="Rigged EPL Table?", font=("Montserrat", 30, "bold italic")).pack()
data = [('No', 'Clubs', 'Points'),
		(1,'Manchester United',20, 'red'),
		(2,'Manchester City',19, 'lightblue'),
		(3,'Tottenham',19, 'grey'),
		(4,'Arzenal',18, 'red'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
		(5,'Brighton',17, 'blue'),
	]

t = TableWidget(baseWindow, data)
t.activate_scrollbar()

baseWindow.mainloop()