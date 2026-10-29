
import unittest
from app import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount()

    def test_initial_balance(self):
        self.assertEqual(self.account.check_balance(), 0.0)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.check_balance(), 500.0)

    def test_multiple_deposits(self):
        self.account.deposit(500)
        self.account.deposit(250)
        self.assertEqual(self.account.check_balance(), 750.0)

    def test_zero_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)


if __name__ == "__main__":
    unittest.main()
