import email
from account import Account

class Driver(Account):
    name = str
    document = str
    id = int
    email = str
    
    def __init__(self, name, document):
        super().__init__(name, document)
