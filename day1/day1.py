import math


def get_fuel_for_mass(mass):
    return math.floor((mass / 3)) - 2


def get_total_fuel_for_mass(mass):
    total_fuel = 0

    while True:
        fuel = max(get_fuel_for_mass(mass), 0)
        total_fuel += fuel

        mass = fuel

        if fuel <= 0:
            return total_fuel


def get_fuel_requirement(masses):
    total_fuel = 0

    for mass in masses:
        total_fuel += get_total_fuel_for_mass(mass)

    return total_fuel


if __name__ == '__main__':
    masses = []

    with open('day1/input') as f:
        masses = [int(i) for i in f.readlines()]

    print(get_fuel_requirement(masses))
