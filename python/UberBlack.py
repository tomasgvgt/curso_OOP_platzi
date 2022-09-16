from asyncio import streams
from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial = []
    model = str

    def __init__(self, licence, driver, typeCarAccepted, seatsMaterial):
        super().__init__(licence, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial

