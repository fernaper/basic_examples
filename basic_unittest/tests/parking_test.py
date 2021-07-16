import inspect
import logging
import unittest
import sys

from os.path import abspath, dirname

# Set python directory on top of tests, so, everything be easily imported
sys.path.insert(0, dirname(dirname(abspath(inspect.getfile(inspect.currentframe())))))

from script.vehicles import Car, Parking, Vehicle, generate_random_vehicles, main

logging.basicConfig(level=logging.DEBUG)


class ParkingTest(unittest.TestCase):
    
    def test_zero_speed(self):
        car = Car()
        car.update_speed()
        self.assertEqual(0, car.current_speed, 'Speed must be 0 if no acceleration')

    def test_positive_acceleration(self):
        car = Car(current_acceleration=10)
        car.update_speed()
        self.assertEqual(10 - 2, car.current_speed)

    def test_negative_acceleration(self):
        car = Car(current_acceleration=-10)
        car.update_speed()
        self.assertEqual(-(10 - 2), car.current_speed)


class FunctionTest(unittest.TestCase):

    def __check_vehicles(self, vehicles):
        for vehicle in vehicles:
            self.assertTrue(isinstance(vehicle, Vehicle))

    def test_generate_random_vehicles(self):
        vehicles = generate_random_vehicles(3)
        self.assertEqual(3, len(vehicles))
        self.__check_vehicles(vehicles)

    def test_main_run(self):
        parking = main(generate_random_vehicles(10))
        self.assertTrue(isinstance(parking, Parking))
        self.__check_vehicles(parking.vehicles)

unittest.main()
