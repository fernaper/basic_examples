import logging
import random
import uuid

from dataclasses import dataclass, field
from typing import List


@dataclass
class Vehicle():
    number_wheels: int
    max_speed: float
    max_acceleration: float
    max_passengers: int
    friction: float
    current_speed: float = 0.0
    current_acceleration: float = 0.0

    def update_speed(self):
        """Calculates speed on next time applying acceleration and friction"""
        change = max(abs(self.current_acceleration) - self.friction, 0)
        if self.current_acceleration < 0:
            self.current_speed -= change
        else:
            self.current_speed += change


@dataclass
class Car(Vehicle):
    number_wheels: float = 4
    max_speed: float = 250
    max_acceleration: float = 50
    max_passengers: int = 5
    friction: float = 2


@dataclass
class Motorbike(Vehicle):
    number_wheels: float = 2
    max_speed: float = 300
    max_acceleration: float = 100
    max_passengers: int = 1
    friction: float = 1


@dataclass
class Parking():
    id: int = field(default_factory=uuid.uuid4)
    vehicles: List[Vehicle] = field(default_factory=list, compare=False, repr=False)


def generate_random_vehicles(number_of_vehicles: int) -> List[Vehicle]:
    return [Car() if bool(random.getrandbits(1)) else Motorbike() for _ in range(number_of_vehicles)]

def main(vehicles: List[Vehicle]) -> None:
    parking = Parking(vehicles=vehicles)
    logging.info(parking)
    logging.debug(
        '\n\n\t'+'\n\t'.join(str(v) for v in parking.vehicles)
    )

    return parking

if __name__ == '__main__': # pragma: no cover
    logging.basicConfig(level=logging.INFO)
    vehicles = generate_random_vehicles(10)
    main(vehicles)
