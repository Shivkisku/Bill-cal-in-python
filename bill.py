import tkinter as tk

class MonthlyBillCalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Monthly Bill Calculator")
        
        # Create the labels and entry fields
        tk.Label(self.window, text="Electricity (kWh):").grid(row=0, column=0)
        self.electricity_entry = tk.Entry(self.window)
        self.electricity_entry.grid(row=0, column=1)
        
        tk.Label(self.window, text="Gas (therms):").grid(row=1, column=0)
        self.gas_entry = tk.Entry(self.window)
        self.gas_entry.grid(row=1, column=1)
        
        tk.Label(self.window, text="Water (gal):").grid(row=2, column=0)
        self.water_entry = tk.Entry(self.window)
        self.water_entry.grid(row=2, column=1)
        
        tk.Label(self.window, text="Internet ($):").grid(row=3, column=0)
        self.internet_entry = tk.Entry(self.window)
        self.internet_entry.grid(row=3, column=1)
        
        tk.Label(self.window, text="Cable TV ($):").grid(row=4, column=0)
        self.cable_entry = tk.Entry(self.window)
        self.cable_entry.grid(row=4, column=1)
        
        tk.Label(self.window, text="Total Bill ($):").grid(row=5, column=0)
        self.total_label = tk.Label(self.window, text="")
        self.total_label.grid(row=5, column=1)
        
        # Create the calculate button
        calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_total)
        calculate_button.grid(row=6, column=1)
        
    def calculate_total(self):
        # Get the input values and convert to floats
        electricity = float(self.electricity_entry.get())
        gas = float(self.gas_entry.get())
        water = float(self.water_entry.get())
        internet = float(self.internet_entry.get())
        cable = float(self.cable_entry.get())
        
        # Calculate the total bill
        total = electricity * 0.12 + gas * 1.5 + water * 0.0025 + internet + cable
        
        # Update the total label
        self.total_label.config(text="{:.2f}".format(total))
        
    def run(self):
        self.window.mainloop()

# Create an instance of the MonthlyBillCalculatorGUI class and run it
gui = MonthlyBillCalculatorGUI()
gui.run()
