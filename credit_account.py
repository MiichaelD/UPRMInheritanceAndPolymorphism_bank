
from account import Account
from terminal_colors import TerminalColors as tc


# Account used to pay but not to withdraw
class CreditAccount(Account):

  def __init__(self, initial_credit=5000):
    Account.__init__(self, 'Credit', balance=initial_credit, can_withdraw=False)
    self.__initial_credit = initial_credit

  # The amount owed to the bank (balance spent)
  def get_balance(self):
    return - (self.__initial_credit - Account.get_available_balance(self)) 

  def deposit(self, amount):
    if amount > abs(self.get_balance()):
      # Can't deposit more than it is owed
      return False
    Account.deposit(self, amount)
    return True

  def transfer_to(self, account, amount):
    print(tc.FAIL, self.get_name(), ': Account not enabled for transfers', tc.ENDC); 
    return False