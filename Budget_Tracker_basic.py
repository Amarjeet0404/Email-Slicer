class BudgetTracker:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = []      # Creating list to store the dictionary of our expenses

    def add_expense(self, description, amount):
        """Add your expense to the tracker."""
        self.expenses.append({'description': description, 'amount': amount})        # Adding expenses to the list
        self.budget -= amount

    def get_remaining_budget(self):
        """Get the remaining budget."""
        return self.budget      # Returning budget after deduction of expenses 

    def print_expenses(self):
        """Print all expenses."""
        for i, expense in enumerate(self.expenses, start=1):
            print(f"    {i}. {expense['description']}: ${expense['amount']}")       # Describing the expense and amount for it

    def credit_salary(self):
        """Credit a new salary to the budget and track expenses."""
        salary = float(input("\nEnter salary amount: "))        # Taking input from the user
        self.budget += salary
        print(f"Salary of ${salary} credited.\nYour budget: ${self.budget}\n")
        self.track_expenses()

    def track_expenses(self):
        """Track expenses."""
        while True:
            description = input("Enter expense description (or type 'quit' to exit): ")         # Taking input from user describing the expense and the amount spent
            if description.lower() == 'quit':
                break
            amount = float(input("Enter expense amount: "))
            self.add_expense(description, amount)
        print("\nExpenses tracked.")

# Example usage
budget_tracker = BudgetTracker(budget=0)

# Credit a new salary
budget_tracker.credit_salary()

# Print remaining budget and expenses
budget_tracker.print_expenses()
print(f"\nRemaining budget: ${budget_tracker.get_remaining_budget()}\n")

print("Do you want to continue tracking expenses? (yes/no)")
if input().lower() == 'yes':        # Condition to re-track the budget
    # Credit a new salary
    budget_tracker.credit_salary()

    # Print remaining budget and expenses
    budget_tracker.print_expenses()
    print(f"Remaining budget: ${budget_tracker.get_remaining_budget()}")
    
else:
    print("\nExiting budget tracker. Have a pleasant day ahead...\n")
