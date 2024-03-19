# finance_record.py

from datetime import datetime

class FinanceRecord:
    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description

class Expense(FinanceRecord):
    def __init__(self, amount, date, description, category):
        super().__init__(amount, date, description)
        self.category = category

class Income(FinanceRecord):
    def __init__(self, amount, date, description, source):
        super().__init__(amount, date, description)
        self.source = source


       
