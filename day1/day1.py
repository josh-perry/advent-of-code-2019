import math


def get_mass_fuel_requirement(mass):
    return math.floor((mass / 3)) - 2


def get_fuel_requirement(masses):
    total_fuel = 0

    for mass in masses:
        total_fuel += get_mass_fuel_requirement(mass)

    return total_fuel


if __name__ == '__main__':
    masses = []

    with open('day1/input') as f:
        masses = [int(i) for i in f.readlines()]

    print(get_fuel_requirement(masses))
