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

        # Create widgets
        title_label = tk.Label(root, text="Budget X", font=("Arial", 20, "bold"), bg="#336699", fg="white")
        title_label.grid(row=0, column=0, columnspan=3, sticky="we", pady=10)

        tk.Label(root, text="Budget:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=10)
        tk.Entry(root, textvariable=self.budget_var, font=("Arial", 14)).grid(row=1, column=1, sticky="w", pady=10)

        tk.Label(root, text="Expenses:", font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=10)
        for i, (name_var, amount_var) in enumerate(self.expenses_vars):
            tk.Entry(root, textvariable=name_var, font=("Arial", 14)).grid(row=i + 2, column=0, sticky="w", pady=5)
            tk.Entry(root, textvariable=amount_var, font=("Arial", 14)).grid(row=i + 2, column=1, sticky="w", pady=5)

        tk.Label(root, text="New Expense:", font=("Arial", 14), bg="#f0f0f0").grid(row=11, column=0, sticky="w", pady=10)
        tk.Entry(root, textvariable=self.new_expense_var, font=("Arial", 14)).grid(row=11, column=1, sticky="w", pady=10)

        tk.Button(root, text="Add Expense", command=self.add_expense, font=("Arial", 14), bg="#336699", fg="white").grid(row=11, column=2, sticky="w", pady=10)

        tk.Label(root, text="Balance:", font=("Arial", 14), bg="#f0f0f0").grid(row=12, column=0, sticky="w", pady=10)
        self.balance_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.balance_label.grid(row=12, column=1, sticky="w", pady=10)

        tk.Button(root, text="Calculate Balance", command=self.calculate_balance, font=("Arial", 14), bg="#336699", fg="white").grid(row=13, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Clear All", command=self.clear_all, font=("Arial", 14), bg="#ff3333", fg="white").grid(row=14, column=0, columnspan=3, pady=10)

        # Set background color
        root.config(bg="#f0f0f0")

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
    root.geometry("400x700")  # Set initial size
    root.mainloop()




