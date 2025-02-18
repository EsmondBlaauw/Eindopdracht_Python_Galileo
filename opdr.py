import csv
from csv import *
import os
from datetime import datetime

# Constants
DATA_FILE = 'test.csv'
categories = []

class ExpenseTracker: # Class Event Tracker
    def __init__(self):
        self.expenses = [] 
        self.categories = {'G', 'T', 'E'}
        self.filename = ""
        self.csvfile = None

    def loading_invoerbestand(self):
        try: 
            with open(DATA_FILE, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                print('Data file opened!')
        except FileNotFoundError:
            print(f"Error: File {DATA_FILE} not found")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
   
        
    def add_expense(self, amount, description, date, category): #1 Function to add expenses
        ...

    def edit_expense(self, index, amount, description, date, category): #2 Function to edit expenses
       ...

    def delete_expense(self, index): #3 Function to delete expenses
       ...

    def add_category(self, category): #4 Functions to add category
        with open(DATA_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            
            if not rows:
                print('NO ROWS!')
                return
            
            headers = rows[0]
            self.categories.update(headers)
            
            if category in self.categories:
                print('Category already exists!')
                return

            self.categories.add(category)

    
    def export_to_excel(self, filename): #5 Function to export data to excel sheet
        ...

    def summary(self):  #6 Summary: Total and SubTotals of expenses
        with open(DATA_FILE, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            # categories.extend(headers)
            self.categories.update(headers)

        for i in range(1, len(categories)):
            print(f"{i}: {categories[i]}")
        csvfile.close()

             
                
    def show_all_expenses(self, filename): #8 Show all expenses
        ...

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    # expense_tracker.loading_invoerbestand()
    # expense_tracker.summary()
    expense_tracker.add_category('JAJAJAJAJA')
    
