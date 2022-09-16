import email
from ssl import _PasswordType
from account import Account

class User(Account):
    id = int
    name = str
    document = str
    email = str

    def __init__(self, name, document):
        super().__init__(name, document)

