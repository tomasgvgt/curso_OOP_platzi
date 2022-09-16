from car import Car
from driver import Driver
from UberX import UberX

if __name__ == '__main__':
    carrito1 = Car('ABC 777', Driver('Calipso', '4'))
    carrito1.print()
    print(vars(carrito1))
    print(vars(carrito1.driver))

    uberX1 = UberX('UBS432', Driver('Homero', '2445656756'), 'seat', 'swift')
    uberX1.print()
    print(vars(uberX1))
    print(vars(uberX1.driver))
    print(uberX1.brand, uberX1.model)
