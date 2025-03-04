import json
import datetime

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.file_name = "expenses.txt"
        self.load_expenses()

    def add_expense(self):
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")
        
        self.expenses.append({"date": date_str, "amount": amount, "category": category, "description": description})
        print("Expense addition succesfull!")

    def view_expenses(self):
        if not self.expenses:
            print("No pre-existing expenses present!")
            return

        print("\nAll Expenses:")
        print("Date        | Amount  | Category       | Description")
        print("----------------------------------------------------")
        for exp in self.expenses:
            print(f"{exp['date']} | {exp['amount']:.2f} | {exp['category']} | {exp['description']}")

    def filter_by_category(self):
        categories = input("Enter categories (comma separated): ").split(',')
        categories = [c.strip() for c in categories]
        filtered = [exp for exp in self.expenses if exp['category'] in categories]
        
        if not filtered:
            print("No expenses found for the given categories.")
            return

        print("\nFiltered Expenses:")
        for exp in filtered:
            print(f"{exp['date']} | {exp['amount']:.2f} | {exp['category']} | {exp['description']}")

    def calculate_average_between_dates(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter date (this is including this entire day) (YYYY-MM-DD): ")

        try:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        filtered = [exp for exp in self.expenses if start <= datetime.datetime.strptime(exp['date'], "%Y-%m-%d").date() <= end]
        
        if not filtered:
            print("No expenses found in the given date range.")
            return

        average = sum(exp['amount'] for exp in filtered) / len(filtered)
        print(f"Average expense between {start_date} and {end_date}: {average:.2f}")

    def delete_expense(self):
        self.view_expenses()
        if not self.expenses:
            return
        
        try:
            index = int(input("Enter the number or index of the expense to delete: "))
            if 0 <= index < len(self.expenses):
                del self.expenses[index]
                print("Expense index deleted!")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

    def save_expenses(self):
        with open(self.file_name, "w") as f:
            json.dump(self.expenses, f)
        print("Expense input saved!")

    def load_expenses(self):
        try:
            with open(self.file_name, "r") as f:
                self.expenses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def menu(self):
        while True:
            print("\nPersonal Expense Manager")
            print("1: Add Expense")
            print("2: View Expenses")
            print("3: Filter by Categories")
            print("4: Calculate Average Between Dates")
            print("5: Delete Expense")
            print("6: Save Expenses")
            print("7: Exit Expense Manager Program")
            
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.filter_by_category()
            elif choice == "4":
                self.calculate_average_between_dates()
            elif choice == "5":
                self.delete_expense()
            elif choice == "6":
                self.save_expenses()
            elif choice == "7":
                self.save_and_exit()
                print("Ending Personal Expense Manager!")
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    ExpenseManager().menu()