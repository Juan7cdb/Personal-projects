class Account:
    id = int
    name = str
    lastname = str
    document = str
    email = str
    password = str 
    
    def __init__(self, id, name, document, lastname, email, password):
        self.name = name
        self.document = document
        self.id = id
        self.lastname = lastname
        self.email = email
        self.password = password