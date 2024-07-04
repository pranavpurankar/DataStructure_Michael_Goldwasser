#!/usr/bin/env python3


class CreditCard:
    '''A consumer credit card'''

    def __init__(self, customer, bank, acnt, limit):
        '''Create a new credit card instance

        The initial balance is zero

        customer: The name of the customer (e.g. 'John Bowman')
        bank: The name of the bank (e.g. 'California Savings')
        acnt: the account indentifier (e.g. '5391 0375 9387 5309')
        limit: credit limit (measured in dollars)
        '''
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        '''Return name of the cutomer'''
        return self._customer

    def get_bank(self):
        '''Return name of the bank'''
        return self._bank

    def get_account(self):
        '''Return card identifying number (typically stored as string)'''
        return self._acnt

    def get_limit(self):
        '''Return the current credit limit'''
        return self._limit

    def get_balance(self):
        '''Return current balance'''
        return self._balance

    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied
        '''
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        '''Process customer payment that reduces balance.'''
        self._balance -= amount


cc = CreditCard('Pranav Purankar', 'Swiss Bank', '0396 4545 9606 2356', 1000)

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Pranav', 'SBI Savings', '5396 5689', 2500))
    wallet.append(CreditCard('Shreyas', 'RBI Savings', '4512 8923', 3500))
    wallet.append(CreditCard('Jasmin', 'SBI Savings', '8923 5620', 500))

    for val in range(1, 17):
        wallet[0].charge(val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank)
        print('Account =', wallet[c].get_account)
        print('Llimit =', wallet[c].get_balance)
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()
