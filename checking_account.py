
from account import Account


class CheckingAccount(Account):

  def __init__(self, initial_amount=1000):
    Account.__init__(self, 'Checking', balance=initial_amount)