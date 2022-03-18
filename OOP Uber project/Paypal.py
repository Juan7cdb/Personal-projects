from Payment import Payment
from Account import Account

class Paypal:
    id = Payment
    name = Account
    lastname = Account
    email = Account
    Password = Account
    
    def __init__(self, id, name, lastname, email, password):
        super.__init__(id, name, lastname)