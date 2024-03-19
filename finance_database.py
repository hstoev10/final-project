# finance_database.py
from logging import Filter
import sqlite3
from warnings import filters
from winreg import QueryValue
from finance_record import Expense, Income

class FinanceDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # Create Expenses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL      
            )
        ''')

        # Create Incomes table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS incomes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                description TEXT NOT NULL,
                source TEXT NOT NULL
            )
        ''')

        # Commit the changes and close the cursor
        self.conn.commit()
        cursor.close()

    def add_record(self, record):
        cursor = self.conn.cursor()

        if isinstance(record, Expense):
            cursor.execute('''
                INSERT INTO expenses (amount, date, description, category)
                VALUES (?, ?, ?, ?)
            ''', (record.amount, record.date, record.description, record.category))
        elif isinstance(record, Income):
            cursor.execute('''
                INSERT INTO incomes (amount, date, description, source)
                VALUES (?, ?, ?, ?)
            ''', (record.amount, record.date, record.description, record.source))

        self.conn.commit()
        cursor.close()

    def get_records(self, filters=None, sorting=None):
        cursor = self.conn.cursor()
        try:
            query = "SELECT * FROM expenses UNION ALL SELECT * FROM incomes"
            if filters:
                filter_conditions = []
                for key, value in filters.items():
                    filter_conditions.append(f"{key} = '{value}'")
                query += " WHERE " + " AND ".join(filter_conditions)
            if sorting:
                sort_conditions = []
                for key, value in sorting.items():
                    sort_conditions.append(f"{key} {value}")
                query += " ORDER BY " + ", ".join(sort_conditions)
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Exception as e:
            print("An error occurred while fetching records:", e)
        finally:
            cursor.close()

    def update_record(self, record_id, updated_record):
        cursor = self.conn.cursor()

        try:
            # Get the existing record
            existing_record = None
            records = self.get_records({"id": record_id})
            if records:
                existing_record = records[0]
            else:
                print("Record not found")
                return

            # Update the record if it exists
            if isinstance(updated_record, Expense):
                cursor.execute('''
                    UPDATE expenses
                    SET amount = ?,
                        date = ?,
                        description = ?,
                        category = ?
                    WHERE id = ?
                ''', (updated_record.amount, updated_record.date, 
                    updated_record.description, updated_record.category, record_id))
            elif isinstance(updated_record, Income):
                cursor.execute('''
                    UPDATE incomes
                    SET amount = ?,
                        date = ?,
                        description = ?,
                        source = ?
                    WHERE id = ?
                ''', (updated_record.amount, updated_record.date, updated_record.description, updated_record.source, record_id))
            else:
                print("Invalid record type")

            self.conn.commit()
            print("Record updated successfully")

        except Exception as e:
            print("An error occurred while updating the record:", e)

        finally:
            cursor.close()
       
       
    def delete_record(self, record_id):
        cursor = self.conn.cursor()

        try:
            # Check if the record exists before deletion
            cursor.execute("SELECT * FROM expenses WHERE id = ?", (record_id,))
            existing_expense = cursor.fetchone()

            cursor.execute("SELECT * FROM incomes WHERE id = ?", (record_id,))
            existing_income = cursor.fetchone()

            if existing_expense:
                cursor.execute("DELETE FROM expenses WHERE id = ?", (record_id,))
                print("Expense record deleted successfully")
            elif existing_income:
                cursor.execute("DELETE FROM incomes WHERE id = ?", (record_id,))
                print("Income record deleted successfully")
            else:
                print("Record not found")

            self.conn.commit()

        except Exception as e:
            print("An error occurred while deleting the record:", e)

        finally:
            cursor.close()