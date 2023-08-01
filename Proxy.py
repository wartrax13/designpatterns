from abc import ABCMeta, abstractmethod
"""
The Proxy design is a estructural pattern.
You we think about object access, we can to used three actors: RealSubject, Subject y Proxy.
Proxy it's a referencial between the Client and RealSubject. 
"""


class You:
    def __init__(self) -> None:
        print('You:: Lets buy the Dnim shirt')
        self.debitCard = DebitCard()
        self.isPurchased = None
    
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    def __del__(self):
        if self.isPurchased:
            print('You:: Wow! Denim shirt is Mine :-)')
        else:
            print('You :: should earn more...')

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    
    def __init__(self) -> None:
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card

        return self.account
    
    def __hasFunds(self):
        print('Bank:: Cheking if Account', self.__getAccount(), 'has enough funds')
    
    def setCard(self, card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print('Bank:: Paying the merchant')
            return True
        else:
            print('Bank:: Sorry, not enogh funds!')
            return False


class DebitCard(Payment):
    def __init__(self) -> None:
        self.bank = Bank()

    def do_pay(self):
        card = input('Proxy::: Punch in Card Number: ')
        self.bank.setCard(card)
        return self.bank.do_pay()


you = You()
you.make_payment()
