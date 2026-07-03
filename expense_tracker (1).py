"""
Expense Tracker - Microproject
Concepts used: Lists, Calculations
"""

expenses = []  # each expense will be a dict: {"name": ..., "amount": ...}


def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return

    expenses.append({"name": name, "amount": amount})
    print(f"Added: {name} - ${amount:.2f}\n")


def display_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")
    print()


def display_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Spending: ${total:.2f}\n")


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Display All Expenses")
        print("3. Display Total Spending")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            display_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
