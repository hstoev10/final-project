# # finance_statistics.py

class FinanceStatistics:
    def __init__(self, database):
        self.database = database

    def get_overall_budget(self):
       
        # Calculate the overall budget by subtracting total expenses from total incomes.
       
        total_incomes = sum([income.amount for income in self.database.get_records() 
        if isinstance(income, income)])
        
        total_expenses = sum([expense.amount for expense in self.database.get_records() 
        if isinstance(expense, expense)])
        return total_incomes - total_expenses

    def get_average_expense(self, period):
        
        # Calculate the average expense for a given period.
        
        records = self.database.get_records()
        total_expenses = sum([expense.amount for expense in records if isinstance(expense, expense)])
        num_expenses = len([expense for expense in records if isinstance(expense, expense)])
        if num_expenses == 0:
            return 0
        return total_expenses / num_expenses

    def get_rundown(self):
        
        # Calculate how many months you can sustain your expenses with your current savings.
      
        overall_budget = self.get_overall_budget()
        if overall_budget <= 0:
            return "You are spending more than you earn."
        average_expense = self.get_average_expense("all")  
        if average_expense == 0:
            return "No expenses recorded."
        return overall_budget / average_expense
