
from terminal_colors import TerminalColors as tc


class Account:

  def __init__(
      self, name, balance=0.0, can_withdraw=True, is_blocked_for_spending=False,):
    self.__name = name
    self.__balance = balance
    self.__is_blocked_for_spending = is_blocked_for_spending
    self.__can_withdraw = can_withdraw

  def get_name(self):
    return self.__name

  # The amount available to spend/withdraw
  def get_available_balance(self):
    return self.__balance

  # This account balance.
  # Depending on type, this can mean owed or owned money.
  def get_balance(self):
    return self.get_available_balance()

  # Deposit the given amount to the account balance.
  def deposit(self, amount):
    self.__balance += amount

  # Withdraws cash from account if amount is below the balance, account is not 
  # blocked and this account can be used for withdraws.
  def withdraw(self, amount):
    if self.is_blocked_for_spending() or not self.can_withdraw():
      print(tc.FAIL, self.get_name(), 'is disabled for withdrawals', tc.ENDC)

    if amount < self.get_available_balance():
      self.__balance - amount;
      return True

    print(tc.FAIL, self.get_name(), ': Not enough balance to withdraw', tc.ENDC)
    return False

  # Transfer money from this account to another
  def transfer_to(self, account, amount):
    if amount <= self.get_available_balance() and account.deposit(amount):
      self.__balance -= amount;
      return True

    print(tc.FAIL, self.get_name(), ': Not enough balance to transfer', tc.ENDC)
    return False

  # Pays for the specified amount if account is not blocked and
  # can afford with balance.
  def pay(self, amount):
    if self.is_blocked_for_spending():
      print(tc.FAIL, self.get_name(), 'is disabled for making payments', tc.ENDC)
      return False

    if amount <= self.get_available_balance():
      self.__balance -= amount;
      return True
    print(tc.FAIL, self.get_name(), ': Not enough balance for payment', tc.ENDC)
    return False

  def can_withdraw(self):
    return self.__can_withdraw and not self.is_blocked_for_spending()

  # Whether the account is disabled for paying/withdrawing.
  # Note that deposits are always allowed even if the account is blocked.
  def is_blocked_for_spending(self):
    return self.__is_blocked_for_spending