
### Persoonlijk Uitgavenbeheer Programma

import json
from datetime import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __repr__(self):
        return f"{self.date} | {self.amount} | {self.category} | {self.description}"

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def add_expense(self):
        date = input("Voer de datum in (YYYY-MM-DD): ")
        amount = input("Voer het bedrag in: ")
        category = input("Voer de categorie in: ")
        description = input("Voer een omschrijving in: ")
        
        if not self.validate_date(date):
            print("Ongeldige datum. Probeer opnieuw.")
            return
        if not self.validate_amount(amount):
            print("Ongeldig bedrag. Probeer opnieuw.")
            return

        expense = Expense(date, float(amount), category, description)
        self.expenses.append(expense)
        print("Deze uitgave is toegevoegd.")

    def view_expenses(self):
        if not self.expenses:
            print("Er zijn geen uitgaven om weer te geven.")
            return
        for idx, expense in enumerate(self.expenses):
            print(f"{idx + 1}: {expense}")

    def filter_by_category(self):
        categories = input("Voer de categorieën in (gescheiden door komma's): ").split(',')
        categories = [cat.strip() for cat in categories]
        filtered_expenses = [exp for exp in self.expenses if exp.category in categories]

        if not filtered_expenses:
            print("Geen uitgaven gevonden voor de opgegeven categorieën.")
        else:
            for expense in filtered_expenses:
                print(expense)

    def calculate_average_between_dates(self):
        start_date = input("Voer de startdatum in (YYYY-MM-DD): ")
        end_date = input("Voer de einddatum in (YYYY-MM-DD): ")

        if not self.validate_date(start_date) or not self.validate_date(end_date):
            print("Ongeldige datum. Probeer opnieuw.")
            return

        total = 0
        count = 0

        for exp in self.expenses:
            if start_date <= exp.date <= end_date:
                total += exp.amount
                count += 1

        if count == 0:
            print("Geen uitgaven gevonden tussen deze datums.")
        else:
            print(f"Gemiddeld bedrag: {total / count:.2f}")

    def remove_expense(self):
        self.view_expenses()
        index = int(input("Voer de index in van de uitgave die je wilt verwijderen: ")) - 1
        
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Uitgave voor deze index is verwijderd.")
        else:
            print("Ongeldig index.")

    def save_expenses(self):
        with open('expenses.txt', 'w') as f:
            json.dump([exp.__dict__ for exp in self.expenses], f)
        print("Uitgaven opgeslagen.")

    def load_expenses(self):
        try:
            with open('expenses.txt', 'r') as f:
                expenses_data = json.load(f)
                self.expenses = [Expense(**item) for item in expenses_data]
        except FileNotFoundError:
            self.expenses = []

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_amount(amount_str):
        try:
            float(amount_str)
            return True
        except ValueError:
            return False

def main():
    manager = ExpenseManager()

    while True:
        print("\nKies een optie:")
        print("1: Uitgaven toevoegen")
        print("2: Uitgaven bekijken")
        print("3: Filteren op categorieën")
        print("4: Gemiddelde berekenen tussen twee datums")
        print("5: Uitgave verwijderen")
        print("6: Opslaan")
        print("7: Afsluiten")

        choice = input("Voer je keuze in: ")

        if choice == '1':#Toevoegen kostenpost
            manager.add_expense()
        elif choice == '2': # Overzicht kostenposten
            manager.view_expenses()
        elif choice == '3': # Filter per 1 of meerdere categorieën 
            manager.filter_by_category()
        elif choice == '4': # Bereken gemiddelde bedrag tussen 2 datums
            manager.calculate_average_between_dates()
        elif choice == '5': # Verwijderen kostenpost
            manager.remove_expense()
        elif choice == '6': # Opslaan kostenpost
            manager.save_expenses()
        elif choice == '7': # Aflsuiten programma
            manager.save_expenses()
            print("Eindigen Persoonlijke Uitgavenbeheer programma!")
            break
        else:
            print("Ongeldige invoer. Probeer opnieuw.")

if __name__ == "__main__":
    main()