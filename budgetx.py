import tkinter as tk

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget X")

        # Initialize variables
        self.budget_var = tk.DoubleVar()
        self.expenses_vars = [(tk.StringVar(), tk.DoubleVar()) for _ in range(8)]  # Increased to 8 for additional fields
        self.new_expense_var = tk.DoubleVar()

        # Set initial values
        self.budget_var.set(0.0)
        for name_var, amount_var in self.expenses_vars:
            name_var.set("")
            amount_var.set(0.0)

        # Create a frame around the entire app
        app_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)  # Adjust pady here
        app_frame.grid(row=0, column=0)

        # Create a frame to hold the title label
        title_frame = tk.Frame(app_frame, bg="#f0f0f0")
        title_frame.grid(row=0, column=0, columnspan=3, pady=10)

        # Create widgets
        title_label = tk.Label(title_frame, text="Budget X - RPM Personal Finance Tracker", font=("Arial", 20, "bold"), bg="#336699", fg="white")
        title_label.grid(row=1, column=0, pady=10, padx=10)

        tk.Label(app_frame, text="Budget:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=10)
        tk.Entry(app_frame, textvariable=self.budget_var, font=("Arial", 14)).grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(app_frame, text="Expenses:", font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=10)
        for i, (name_var, amount_var) in enumerate(self.expenses_vars):
            tk.Entry(app_frame, textvariable=name_var, font=("Arial", 14)).grid(row=i + 2, column=0, sticky="w", pady=5)
            tk.Entry(app_frame, textvariable=amount_var, font=("Arial", 14)).grid(row=i + 2, column=1, sticky="w", pady=5)

        tk.Label(app_frame, text="New Expense:", font=("Arial", 14), bg="#f0f0f0").grid(row=11, column=0, sticky="w", pady=10)
        tk.Entry(app_frame, textvariable=self.new_expense_var, font=("Arial", 14)).grid(row=11, column=1, sticky="w", pady=10)

        tk.Button(app_frame, text="Add Expense", command=self.add_expense, font=("Arial", 14), bg="#336699", fg="white").grid(row=11, column=2, sticky="w", pady=10)

        tk.Label(app_frame, text="Balance:", font=("Arial", 14), bg="#f0f0f0").grid(row=12, column=0, sticky="w", pady=10)
        self.balance_label = tk.Label(app_frame, text="", font=("Arial", 14), bg="#f0f0f0")
        self.balance_label.grid(row=12, column=1, sticky="w", pady=10)

        tk.Button(app_frame, text="Calculate Balance", command=self.calculate_balance, font=("Arial", 14), bg="#336699", fg="white").grid(row=13, column=0, pady=10)
        tk.Button(app_frame, text="Clear All", command=self.clear_all, font=("Arial", 14), bg="#ff3333", fg="white").grid(row=13, column=2, pady=10)

    def add_expense(self):
        new_expense = self.new_expense_var.get()
        for name_var, amount_var in self.expenses_vars:
            name = name_var.get()
            amount = amount_var.get()
            if name and amount:
                amount_var.set(amount + new_expense)
        self.new_expense_var.set(0.0)

    def calculate_balance(self):
        budget = self.budget_var.get()
        expenses = sum(amount_var.get() for _, amount_var in self.expenses_vars)
        balance = budget - expenses
        self.balance_label.config(text=f"Balance: ${balance:.2f}")

    def clear_all(self):
        self.budget_var.set(0.0)
        for name_var, amount_var in self.expenses_vars:
            name_var.set("")
            amount_var.set(0.0)
        self.new_expense_var.set(0.0)
        self.balance_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.geometry("600x800")  # Set initial size
    root.mainloop()










