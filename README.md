# Bill-cal-in-python

This is a Python program that creates a graphical user interface (GUI) for a monthly bill calculator. The GUI includes entry fields for inputting the amounts of electricity, gas, water, internet, and cable TV used, as well as a button to calculate the total bill. The program uses the tkinter module to create the GUI.

When the user clicks the calculate button, the program retrieves the input values and calculates the total bill based on the following formula:

total = electricity * 0.12 + gas * 1.5 + water * 0.0025 + internet + cable

The total bill is then displayed in a label on the GUI.

To run the program, an instance of the MonthlyBillCalculatorGUI class is created and its run method is called. The program then enters a loop to display the GUI and wait for user input.




