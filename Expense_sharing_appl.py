import tkinter as tk
from tkinter import messagebox

class ExpenseSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Sharing App")
        self.root.geometry("400x400")
        self.root.configure(bg='#f0f0f0')

        self.expenses = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Expense Sharing App", font=("Helvetica", 16), bg='#f0f0f0', fg='#333333')
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self.root, text="Name:", bg='#f0f0f0', fg='#333333')
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.amount_label = tk.Label(self.root, text="Amount:", bg='#f0f0f0', fg='#333333')
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense, bg='#4CAF50', fg='white')
        self.add_button.pack(pady=10)

        self.calculate_button = tk.Button(self.root, text="Calculate Splits", command=self.calculate_splits, bg='#2196F3', fg='white')
        self.calculate_button.pack(pady=10)

        self.result_text = tk.Text(self.root, height=10, width=40, bg='#e0e0e0', fg='#333333')
        self.result_text.pack(pady=10)

    def add_expense(self):
        name = self.name_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid amount")
            return
        
        if name and amount:
            self.expenses.append((name, amount))
            self.name_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            messagebox.showinfo("Expense Added", f"Added {amount} by {name}")
        else:
            messagebox.showerror("Input Error", "Please fill in all fields")

    def calculate_splits(self):
        if not self.expenses:
            messagebox.showinfo("No Expenses", "No expenses to split")
            return

        total_amount = sum(amount for name, amount in self.expenses)
        num_people = len(set(name for name, amount in self.expenses))
        split_amount = total_amount / num_people

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Total Amount: ${total_amount:.2f}\n")
        self.result_text.insert(tk.END, f"Each person should pay: ${split_amount:.2f}\n\n")

        balances = {}
        for name, amount in self.expenses:
            if name not in balances:
                balances[name] = 0
            balances[name] += amount - split_amount

        for name, balance in balances.items():
            if balance > 0:
                self.result_text.insert(tk.END, f"{name} should receive ${balance:.2f}\n")
            elif balance < 0:
                self.result_text.insert(tk.END, f"{name} should pay ${-balance:.2f}\n")
            else:
                self.result_text.insert(tk.END, f"{name} is settled\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseSharingApp(root)
    root.mainloop()
