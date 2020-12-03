
from account import Account


# Savings account allows clients to save money but not to spend or withdraw.
class SavingsAccount(Account):

  def __init__(self, initial_amount=0, interest_rate=0.025):
    Account.__init__(
      self, 'Savings', balance=initial_amount, is_blocked_for_spending=True)
    self.__interest_rate = interest_rate

  def accrue_interest(self):
    interest = Account.get_balance(self) * self.__interest_rate
    Account.deposit(self, interest)
