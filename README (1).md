# 💰 Expense Tracker

A simple command-line Expense Tracker built in Python. Add your daily expenses and instantly see your total spending.

## Features

- ➕ Add expenses (name + amount)
- 📋 Display all recorded expenses
- 💵 Display total spending
- 🚪 Simple menu-driven interface

## Concepts Used

- **Lists** — storing expenses as a list of dictionaries
- **Calculations** — using `sum()` to compute total spending

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Run the project

```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker.git
cd expense-tracker
python expense_tracker.py
```

## Usage

When you run the script, you'll see a menu:

```
===== Expense Tracker =====
1. Add Expense
2. Display All Expenses
3. Display Total Spending
4. Exit
```

Choose an option by typing the number and pressing Enter.

## Example

```
Choose an option (1-4): 1
Enter expense name: Coffee
Enter amount: 4.50
Added: Coffee - $4.50

Choose an option (1-4): 3
Total Spending: $4.50
```

## Future Improvements

- [ ] Save expenses to a file (CSV/JSON) so data persists
- [ ] Add expense categories
- [ ] Filter expenses by date or category
- [ ] Build a GUI or web version

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
