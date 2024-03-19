import unittest
from unittest.mock import patch, MagicMock
from finance_manager import FinanceManager

class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.finance_manager = FinanceManager()

    def test_create_account(self):
        
        # arrange
        initial_balance = 500  
        account_id = '321'
        
        # act
        self.finance_manager.create_account(account_id,initial_balance)

        # assert
        self.assertTrue(account_id in self.finance_manager.get_all_accounts()) 
        self.assertEqual(self.finance_manager.get_account_balance(account_id), initial_balance)  
        
        

    def test_close_account(self):
       
        account_id= '123'
       
        self.finance_manager.create_account(account_id,100)

        self.finance_manager.close_account(account_id)

        self.assertTrue(account_id not in self.finance_manager.get_all_accounts()) 
        

        

    # def test_get_account_balance(self):
    #     self.assertEqual(get_account_balance(), expected_balance)

        

    def close_account():
        return True
    
    def get_account_balance():
        return 500
    


    @patch('requests.get')
    def test_get_customer_credit_score(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"credit_score": 1}

        credit_score = self.finance_manager.get_customer_credit_score("321")

        self.assertEqual(1, credit_score)



if __name__ == '__main__':
    unittest.main()
