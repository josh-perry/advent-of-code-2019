import math


def get_module_fuel_requirement(mass):
    return math.floor((mass / 3)) - 2


def get_fuel_requirement():
    total_fuel = 0

    with open('day1/input') as f:
        lines = f.readlines()

        for line in lines:
            mass = int(line)
            total_fuel += get_module_fuel_requirement(mass)

    return total_fuel


if __name__ == '__main__':
    print(get_fuel_requirement())
