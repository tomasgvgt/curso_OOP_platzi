from account import Account

class Car:
    '''
    Class that represents an uber car
    '''
    id = int
    license = str
    driver = Account("","")
    passenger = str
    def __init__(self, licence, driver):
        self.licence = licence
        self.driver = driver

    def print(self):
        print(f'Car info. Licence: {self.licence}, driver name: {self.driver.name}, driver document: {self.driver.document}')

