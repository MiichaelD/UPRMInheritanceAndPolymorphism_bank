
from checking_account import CheckingAccount
from credit_account import CreditAccount
from savings_account import SavingsAccount
from terminal_colors import TerminalColors as tc

def main():
  checking = CheckingAccount(initial_amount=100)
  savings = SavingsAccount(initial_amount=1000)
  credit = CreditAccount(initial_credit=500)
  all_accounts = [checking, savings, credit]
  print_statement(all_accounts, header='Opened new accounts')

  # Try buying phone with Savings account, if not possible pay with Credit.
  print(tc.HEADER, 'Trying to buy a new phone', tc.ENDC)
  phone_price = 460
  if not savings.pay(phone_price):
    if credit.pay(phone_price):
      print('Made payment with Credit card. Item worth $', phone_price, '\n')
  print_statement(all_accounts, 'New balances after paying for phone')

  # A month later
  _fast_forward_a_month(checking, savings, credit)
  print_statement(all_accounts)
  
  # # Paying credit card
  checking.transfer_to(credit, 300)
  savings.transfer_to(credit, 25)
  print_statement(all_accounts,'Pay credit card from checking and savings accounts')


def _fast_forward_a_month(checking, savings, credit):
  print(tc.HEADER, 'A month later: Employer deposited, savings generated interests and paid phone bill', tc.ENDC)
  phone_bill = 40
  checking.deposit(1000)
  savings.accrue_interest()
  credit.pay(phone_bill)

def print_account_info(account):
  print(account.get_name())
  # Some types of accounts have different balance than available balance
  if account.get_balance() != account.get_available_balance():
    print(tc.OKGREEN if account.get_available_balance() >= 0 else tc.FAIL,
          '\tAvailable Balance:', account.get_available_balance(), tc.ENDC)

  print(tc.FAIL if account.get_balance() < 0 else tc.OKGREEN, 
        '\tBalance:', account.get_balance(), tc.ENDC)

  if account.is_blocked_for_spending():
    print('\tCannot be used for spending')

  if not account.can_withdraw():
    print('\tCannot be used for withdrawing cash')

def print_statement(accounts, header=None):
  if header is not None:
    print(tc.HEADER, header, tc.ENDC)
  for account in accounts:
    print_account_info(account)
    print()
  print()
  

# Run the program
main()