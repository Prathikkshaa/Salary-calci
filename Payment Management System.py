import tkinter as tk
from tkinter import font

class Employee:
    def __init__(self, emp_id, name, base_pay, deductions=0, bonuses=0):
        self.emp_id = emp_id
        self.name = name
        self.base_pay = base_pay
        self.deductions = deductions
        self.bonuses = bonuses

    def calculate_salary(self):
        gross_salary = self.base_pay + self.bonuses - self.deductions
        tax_rate = 0.2  # Example tax rate
        taxes = gross_salary * tax_rate
        net_salary = gross_salary - taxes
        return net_salary


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_payroll(self):
        print("Processing Payroll...")
        for employee in self.employees:
            net_salary = employee.calculate_salary()
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Net Salary: ₹{net_salary:.2f}")  # Changed currency to INR


class EmployeePaymentManagementSystemUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Payment Management System")
        self.master.configure(bg='black')
        self.master.geometry("500x400")  # Larger window size

        self.label_font = font.Font(family="Times New Roman", size=12, weight="bold")
        self.entry_font = font.Font(family="Times New Roman", size=10)

        self.emp_id_label = tk.Label(master, text="Employee ID:", font=self.label_font, fg="white", bg="black")
        self.emp_id_label.grid(row=0, column=0, sticky="e")
        self.emp_id_entry = tk.Entry(master, font=self.entry_font)
        self.emp_id_entry.grid(row=0, column=1)

        self.name_label = tk.Label(master, text="Name:", font=self.label_font, fg="white", bg="black")
        self.name_label.grid(row=1, column=0, sticky="e")
        self.name_entry = tk.Entry(master, font=self.entry_font)
        self.name_entry.grid(row=1, column=1)

        self.base_pay_label = tk.Label(master, text="Base Pay:", font=self.label_font, fg="white", bg="black")
        self.base_pay_label.grid(row=2, column=0, sticky="e")
        self.base_pay_entry = tk.Entry(master, font=self.entry_font)
        self.base_pay_entry.grid(row=2, column=1)

        self.deductions_label = tk.Label(master, text="Deductions:", font=self.label_font, fg="white", bg="black")
        self.deductions_label.grid(row=3, column=0, sticky="e")
        self.deductions_entry = tk.Entry(master, font=self.entry_font)
        self.deductions_entry.grid(row=3, column=1)

        self.bonuses_label = tk.Label(master, text="Bonuses:", font=self.label_font, fg="white", bg="black")
        self.bonuses_label.grid(row=4, column=0, sticky="e")
        self.bonuses_entry = tk.Entry(master, font=self.entry_font)
        self.bonuses_entry.grid(row=4, column=1)

        self.add_employee_button = tk.Button(master, text="Add Employee", font=self.label_font, command=self.add_employee)
        self.add_employee_button.grid(row=5, columnspan=2)

        self.process_payroll_button = tk.Button(master, text="Process Payroll", font=self.label_font, command=self.process_payroll)
        self.process_payroll_button.grid(row=6, columnspan=2)

    def add_employee(self):
        try:
            emp_id = int(self.emp_id_entry.get())
            name = self.name_entry.get()
            base_pay = float(self.base_pay_entry.get())
            deductions = float(self.deductions_entry.get())
            bonuses = float(self.bonuses_entry.get())

            employee = Employee(emp_id, name, base_pay, deductions, bonuses)
            payroll_system.add_employee(employee)
            print(f"Employee {name} added successfully.")
        except ValueError:
            print("Invalid input")

    def process_payroll(self):
        payroll_system.process_payroll()


def main():
    root = tk.Tk()
    global payroll_system  # Making payroll_system accessible within the UI class
    payroll_system = PayrollSystem()
    app = EmployeePaymentManagementSystemUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
