from Payment import Payment
from Account import Account

class Card:
    id = Payment
    name = Account
    lastname = Account
    cvv = int
    date = str
    
    def __init__(self, id, name, lastname, cvv, date):
        super.__init__(id, name, lastname)
        self.cvv = cvv
        self.date = date