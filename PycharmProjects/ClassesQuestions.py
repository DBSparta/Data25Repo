print("\nQ1a\n")
# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:


class Country:
    def __init__(self, name, continent, climate, language, landlocked):
        self.name = name
        self.continent = continent
        self.climate = climate
        self.language = language
        self.landlocked = landlocked


country1 = Country('Nederland', 'Europe', 'Temperate Oceanic', 'Dutch', 'False')

print("\nQ1b\n")
# Q1b: Create a subclass of a city which inherits from the country class

# A1b:


class City(Country):
    def __init__(self, capital, population, city_name, name, continent, climate, language, landlocked):
        super().__init__(name, continent, climate, language, landlocked)
        self.capital = capital
        self.population = population
        self.city_name = city_name


city1 = City(False, 600000, 'Rotterdam', 'Nederland', 'Europe', 'Temperate Oceanic', 'Dutch', 'False')

print(city1.population)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


# A2a:


z = []
for x in list_of_numbers:
    y = Number(x)
    if y.is_prime():
        z.append(x)
print(z)


print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above


# A2b:

z = []
for x in list_of_numbers:
    y = Number(x)
    if y.divisible_by_n(3) and y.divisible_by_n(4):
        z.append(x)
print(z)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
        print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:


# -------------------------------------------------------------------------------------- #
x = '2737'


def compute_check_digit(identification_number):
    x = 0
    for i in range(0, int(len(identification_number)/2)):
        x += int(str(identification_number)[2 * i])
    x = x * 3
    for j in range(0, int(len(identification_number)/2)-1):
        x += int(str(identification_number)[2 * i + 1])
    x = int(str(x)[-1])
    if x != 0:
        x = 10 - x
    return x


import random


def lucky_money(money, giftees):
    y = 0
    if money < giftees:
        y = 0
    if money >= 8 * giftees:
        y = giftees
    else:
        while money > 8 and money > giftees:
            money -= 8
            y = y + 1
    return y


print(lucky_money(32, 4))










