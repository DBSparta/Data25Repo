print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def f1(x: int) -> list:
    s1 = []
    for y in range(1, int(x/2)+1):
        if x % y == 0:
            s1.append(y)
    s1.append(x)
    return s1


print(f1(3))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:


def f2(x: int, y: int) -> int:
    if y in f1(x):
        return True
    else:
        return False


print(f2(6, 3))
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:


def f3(x: str):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    if len(x) == 1:
        return alphabet.index(x.lower())
    else:
        return 'error'


print(f3('ab'))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:


def f4(x: str) -> str:
    z = ''
    for y in x:
        z = z + str(f3(y))
    return z


print(f4('bob'))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


def f6(x):
    z = 0
    for y in f4(x):
        z += int(y)
    return int(f4(x)) - z


print(f6('bob'))
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:


def f7(x):
    for y in range(2, int(x / 2)):
        if x % y == 0:
            return False
    else:
        return True


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


def f8(x):
    if type(x) == int:
        return f7(x)
    else:
        return 'Invalid Input'


print(f8(5))
# -------------------------------------------------------------------------------------- #






