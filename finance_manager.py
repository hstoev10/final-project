# finance_manager.py

from finance_database import FinanceDatabase
from finance_statistics import FinanceStatistics
from finance_record import Expense, Income

class FinanceManager:
    def __init__(self):
        self.database = FinanceDatabase()
        self.statistics = FinanceStatistics(self.database)
        
    
    def run(self):
        while True:
            print("\n===== Finance Manager =====")
            print("1. Add Expense")
            print("2. Add Income")
            print("3. View Records")
            print("4. View Statistics")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.add_income()
            elif choice == "3":
                self.view_records()
            elif choice == "4":
                self.view_statistics()
            elif choice == "5":
                print("Exiting Finance Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def add_expense(self):
        amount = float(input("Enter the expense amount: "))
        date = input("Enter the expense date (YYYY-MM-DD): ")
        description = input("Enter a description for the expense: ")
        category = input("Enter the expense category: ")

        expense = Expense(amount, date, description, category)
        self.database.add_record(expense)
        print("Expense added successfully.")

    def add_income(self):
        amount = float(input("Enter the income amount: "))
        date = input("Enter the income date (YYYY-MM-DD): ")
        description = input("Enter a description for the income: ")
        source = input("Enter the income source: ")

        income = Income(amount, date, description, source)
        self.database.add_record(income)
        print("Income added successfully.")

    def view_records(self):
        records = self.database.get_records()
        print("\n===== All Records =====")
        for record in records:
            print(record.__dict__)

    def view_statistics(self):
        overall_budget = self.statistics.get_overall_budget()
        average_expense = self.statistics.get_average_expense("2024-01-01")  # Replace with the desired period
        rundown = self.statistics.get_rundown()

        print("\n===== Statistics =====")
        print(f"Overall Budget: ${overall_budget}")
        print(f"Average Expense: ${average_expense}")
        print(f"Rundown: {rundown} months without income")
