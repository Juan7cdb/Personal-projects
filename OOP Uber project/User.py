from Account import Account

class User(Account):
    def __init__(self, id, name, document, lastname, email, password):
        super.__init__(id, name, document, lastname, email, password)